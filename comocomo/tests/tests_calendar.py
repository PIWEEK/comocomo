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

    def test_calendar_with_bad_dates(self):
        with self.assertRaises(ValueError):
            cal = Calendar(year=2013, month=0, day=99)
        with self.assertRaises(TypeError):
            cal = Calendar(year=2013, month=1, day='error')
        with self.assertRaises(TypeError):
            cal = Calendar(year=2013)

    def test_today(self):
        cal = Calendar()
        self.assertEqual(cal.today, date.today())
        cal = Calendar(year=2013, month=7, day=16)
        self.assertEqual(cal.today, date.today())

    def test_current_week(self):
        cal = Calendar(year=2013, month=7, day=16)
        week = cal.current_week
        self.assertEqual(len(week), 7)
        self.assertEqual(week[0], date(year=2013, month=7, day=15))
        self.assertEqual(week[1], date(year=2013, month=7, day=16))
        self.assertEqual(week[2], date(year=2013, month=7, day=17))
        self.assertEqual(week[3], date(year=2013, month=7, day=18))
        self.assertEqual(week[4], date(year=2013, month=7, day=19))
        self.assertEqual(week[5], date(year=2013, month=7, day=20))
        self.assertEqual(week[6], date(year=2013, month=7, day=21))

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

