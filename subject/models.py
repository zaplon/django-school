# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models

from account.models import Student, Teacher


class SubjectTemplate(models.Model):
    class Meta:
        verbose_name = _('Subject template')
    name = models.CharField(max_length=256, verbose_name=_('name'))
    slug = models.SlugField()
    per_week = models.IntegerField(default=0, verbose_name=_('lessons per week'))
    duration = models.IntegerField(default=45, verbose_name=_('duration'))


class SubjectEnrolment(models.Model):
    class Meta:
        verbose_name = _('subject enrolment')
        verbose_name_plural = _('subject enrolments')
    start_date = models.DateField(verbose_name=_('start date'))
    end_date = models.DateField(verbose_name=_('end date'))
    subject = models.ForeignKey('Subject', verbose_name=_('subject'))


class StudentEnrolment(SubjectEnrolment):
    student = models.ForeignKey(Student)


class TeacherEnrolment(SubjectEnrolment):
    teacher = models.ForeignKey(Teacher)


class Subject(SubjectTemplate):
    class Meta:
        verbose_name = _('Subject')
    students = models.ManyToManyField(Student, through=StudentEnrolment, related_name='subjects', verbose_name=_('students'))
    teachers = models.ManyToManyField(Teacher, through=TeacherEnrolment, related_name='subjects', verbose_name=_('teachers'))


