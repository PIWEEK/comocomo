# -*- coding: utf-8 -*-

from django.views.generic.base import View, TemplateView
from django.utils.translation import ugettext as _
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

import datetime
import json

from calendar import Calendar
from models import FoodKind, FoodType, SlotType, DaySlot

class FoodKindsView(View):

    def get(self, request):
        food_kinds_data = [food_kind.to_dict() for food_kind in FoodKind.objects.all()]
        return HttpResponse(json.dumps(food_kinds_data), content_type='application/json')

class FoodTypesView(View):

    def get(self, request):
        food_types_data = [food_type.to_dict() for food_type in FoodType.objects.all()]
        return HttpResponse(json.dumps(food_types_data), content_type='application/json')


class WeekView(TemplateView):

    template_name = 'comocomo/week.html'

    def get(self, request):

        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        day = request.GET.get('day', None)
        try:
            self.calendar = Calendar(
                year = int(year) if year else None,
                month = int(month) if month else None,
                day = int(day) if day else None,
            )
        except (TypeError, ValueError):
            raise ValueError(_(u'Fecha incorrecta: {}/{}/{}'.format(day, month, year)))

        self.week= []
        for date in self.calendar.current_week:
            day_slots = []
            for slot in SlotType.values():
                try:
                    day_slot = DaySlot.objects.get(user=request.user, date=date, slot=slot)
                except DaySlot.DoesNotExist:
                    day_slot = DaySlot(user=request.user, date=date, slot=slot)
                day_slots.append(day_slot)
            self.week.append((date, day_slots))

        return super(WeekView, self).get(request)

    def get_context_data(self, **kwargs):
        context = super(WeekView, self).get_context_data(**kwargs)
        context['calendar'] = self.calendar
        context['week'] = self.week
        return context


class SlotView(TemplateView):

    template_name = 'comocomo/slot.html'

    def get(self, request):

        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        day = request.GET.get('day', None)
        slot = request.GET.get('slot', None)
        try:
            self.current_date = datetime.date(
                year = int(year),
                month = int(month),
                day = int(day),
            )
        except (TypeError, ValueError):
            raise ValueError(_(u'Fecha incorrecta: {}/{}/{}'.format(day, month, year)))

        try:
            if not int(slot) in SlotType.values():
                raise ValueError()
        except ValueError:
            raise ValueError(_(u'Período incorrecto: {}'.format(slot)))

        try:
            self.day_slot = DaySlot.objects.get(user=request.user, date=self.current_date, slot=int(slot))
        except DaySlot.DoesNotExist:
            self.day_slot = DaySlot(user=request.user, date=self.current_date, slot=int(slot))

        return super(SlotView, self).get(request)

    def get_context_data(self, **kwargs):
        context = super(SlotView, self).get_context_data(**kwargs)
        context['current_date'] = self.current_date
        context['all_kinds'] = FoodKind.objects.all()
        context['day_slot'] = self.day_slot
        return context


class SlotEatenView(View):

    def dispatch(self, request, *args, **kwargs):

        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        day = request.GET.get('day', None)
        slot = request.GET.get('slot', None)
        try:
            self.current_date = datetime.date(
                year = int(year),
                month = int(month),
                day = int(day),
            )
        except (TypeError, ValueError):
            raise ValueError(_(u'Fecha incorrecta: {}/{}/{}'.format(day, month, year)))

        try:
            self.slot_type = int(slot)
            if not self.slot_type in SlotType.values():
                raise ValueError()
        except ValueError:
            raise ValueError(_(u'Período incorrecto: {}'.format(slot)))

        try:
            self.day_slot = DaySlot.objects.get(user=request.user, date=self.current_date, slot=self.slot_type)
        except DaySlot.DoesNotExist:
            self.day_slot = None

        return super(SlotEatenView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        eaten = [food_type.id for food_type in self.day_slot.eaten.all()] if self.day_slot else []
        return HttpResponse(json.dumps(eaten), content_type='application/json')

    def post(self, request, *args, **kwargs):
        food_types = []
        for name, value in request.POST.items():
            if name.startswith('select-type'):
                try:
                    food_type = FoodType.objects.get(id = value)
                    food_types.append(food_type)
                except FoodType.DoesNotExist:
                    raise Http404(_(u'No se encuentra FoodType con id {}'.format(value)))

        if not self.day_slot:
            self.day_slot = DaySlot.objects.create(
                user=request.user,
                date=self.current_date,
                slot=self.slot_type,
            )

        self.day_slot.eaten.clear()
        for food_type in food_types:
            self.day_slot.eaten.add(food_type)

        return HttpResponseRedirect(
            reverse('week') + "?year={}&month={}&day={}".format(
                self.current_date.year,
                self.current_date.month,
                self.current_date.day,
            )
        )

