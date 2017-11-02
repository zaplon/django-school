# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from timetable.models import Timetable


class TimetableTestCase(TestCase):

    def setUp(self):
        self.timetable = Timetable.objects.create(name='test')

    def test_creating_timetable_creates_version(self):
        self.assertIsNotNone(self.timetable.latest_version)
