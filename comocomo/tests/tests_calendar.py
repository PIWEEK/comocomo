# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import date, timedelta

from ..calendar import *

class TestCalendar(TestCase):

    def test_emtpy_calendar(self):
        cal = Calendar()
        self.assertEqual(cal.current_date, date.today())

    def test_calendar_with_date(self):
        cal = Calendar(year=2013, month=7, day=16)
        self.assertEqual(cal.current_date, date(year=2013, month=7, day=16))

    def test_start_of_week(self):
        cal = Calendar(year=2013, month=7, day=16)
        self.assertEqual(cal.start_of_week, date(year=2013, month=7, day=15))

    def test_end_of_week(self):
        cal = Calendar(year=2013, month=7, day=16)
        self.assertEqual(cal.end_of_week, date(year=2013, month=7, day=21))

    def test_minus_one_week(self):
        cal = Calendar(year=2013, month=7, day=16)
        self.assertEqual(cal.minus_one_week, date(year=2013, month=7, day=9))

    def test_plus_one_week(self):
        cal = Calendar(year=2013, month=7, day=16)
        self.assertEqual(cal.plus_one_week, date(year=2013, month=7, day=23))

