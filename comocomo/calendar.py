# -*- coding: utf-8 -*-

from datetime import date, timedelta

class Calendar(object):

    def __init__(self, year=None, month=None, day=None):
        if not year or not month or not day:
            self._current_date = date.today()
        else:
            self._current_date = date(year=year, month=month, day=day)

    @property
    def current_date(self):
        return self._current_date

    @property
    def start_of_week(self):
        return self._current_date - timedelta(days=self._current_date.weekday())

    @property
    def end_of_week(self):
        return self._current_date + timedelta(days=(6 - self._current_date.weekday()))

    @property
    def minus_one_week(self):
        return self._current_date - timedelta(days=7)

    @property
    def plus_one_week(self):
        return self._current_date + timedelta(days=7)
