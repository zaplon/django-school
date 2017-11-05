# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase

from account.models import Teacher, Student
from subject.models import Subject, TeacherEnrolment, StudentEnrolment
from timetable.models import Timetable
from model_mommy import mommy


class TimetableTestCase(TestCase):

    def setUp(self):
        user_1 = mommy.make(User)
        user_2 = mommy.make(User)
        teacher = mommy.make(Teacher, user=user_1)
        student = mommy.make(Student, user=user_2)
        subject = mommy.make(Subject, per_week=5)
        mommy.make(StudentEnrolment, subject=subject, student=student)
        mommy.make(TeacherEnrolment, subject=subject, teacher=teacher)
        self.timetable = Timetable.objects.create(name='test')

    def test_creating_timetable_creates_version(self):
        self.assertIsNotNone(self.timetable.latest_version)

    def test_creating_timetable_version_creates_cards(self):
        self.assertEqual(self.timetable.latest_version.cards.count(), 5)
