# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from datetime import date, timedelta

from calendar import Calendar

class WeekView(TemplateView):

    template_name = 'comocomo/week.html'

    def get(self, request, year=None, month=None, day=None):
        self.calendar = Calendar(
            year = int(year) if year != None else None,
            month = int(month) if month != None else None,
            day = int(day) if day != None else None,
        )
        return super(WeekView, self).get(request)

    def get_context_data(self, **kwargs):
        context = super(WeekView, self).get_context_data(**kwargs)
        context['calendar'] = self.calendar
        return context
