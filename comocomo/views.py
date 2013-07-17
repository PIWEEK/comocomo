# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from datetime import date, timedelta

from calendar import Calendar
from models import SlotType, DaySlot

class WeekView(TemplateView):

    template_name = 'comocomo/week.html'

    def get(self, request, year=None, month=None, day=None):

        self.calendar = Calendar(
            year = int(year) if year != None else None,
            month = int(month) if month != None else None,
            day = int(day) if day != None else None,
        )

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
