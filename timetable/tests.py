# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase

from account.models import Teacher, Student
from subject.models import Subject
from timetable.models import Timetable
from model_mommy import mommy


class TimetableTestCase(TestCase):

    def setUp(self):
        self.timetable = Timetable.objects.create(name='test')
        user_1 = mommy.make(User)
        user_2 = mommy.make(User)
        teacher = mommy.make(Teacher, user=user_1)
        student = mommy.make(Student, user=user_1)
        subject = Subject.objects.create(name='test', per_week=5)
        subject.teachers.add(teacher)
        subject.students.add(student)

    def test_creating_timetable_creates_version(self):
        self.assertIsNotNone(self.timetable.latest_version)

    def test_creating_timetable_version_creates_cards(self):
        self.assertEqual(self.timetable.latest_version.cards.count(), 5)
