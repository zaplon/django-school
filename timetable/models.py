# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from account.models import Student, Teacher
from subject.models import Subject


class Lesson(models.Model):
    class Meta:
        verbose_name = _('Lesson')
    subject = models.ForeignKey(Subject, related_name='lessons')
    topic = models.CharField(max_length=256, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)


PRESENCE_TYPES = (('present', _('present')), ('absent', _('absent')), ('excused', _('excused')))


class Presence(models.Model):
    class Meta:
        verbose_name = _('Presence')
    lesson = models.ForeignKey(Lesson, related_name='presences')
    status = models.CharField(choices=PRESENCE_TYPES, verbose_name=_('status'), max_length=16)


class StudentPresence(Presence):
    student = models.ForeignKey(Student)


class TeacherPresence(Presence):
    teacher = models.ForeignKey(Teacher)


class Timetable(models.Model):
    class Meta:
        verbose_name = _('Timetable')
    name = models.CharField(max_length=256, verbose_name=_('name'))

    @property
    def latest_version(self):
        return self.versions.latest()


@receiver(post_save, sender=Timetable)
def create_version(sender, instance, created, **kwargs):
    if created:
        TimetableVersion.objects.create(parent=instance, number=1)


class TimetableVersion(models.Model):
    class Meta:
        get_latest_by = 'number'
    number = models.IntegerField()
    parent = models.ForeignKey(Timetable, related_name=_('versions'))

    def create_cards(self):
        subjects = Subject.objects.all()
        records = []
        for s in subjects:
            for i in range(0, s.per_week):
                records.append(Card(duration=s.duration, timetable_version=self))
        cards = Card.objects.bulk_create(records)
        for c in cards:
            c.students.set(s.students)
            c.teachers.set(s.teachers)


@receiver(post_save, sender=TimetableVersion)
def create_version(sender, instance, created, **kwargs):
    if created:
        instance.create_cards()


class Card(models.Model):
    class Meta:
        verbose_name = _('Card')
    students = models.ManyToManyField(Student, related_name='terms', verbose_name=_('students'))
    teachers = models.ManyToManyField(Teacher, related_name='terms', verbose_name=_('teachers'))
    day_of_week = models.IntegerField(verbose_name=_('day of week'), blank=True, null=True)
    time = models.TimeField(verbose_name=_('hour'), blank=True, null=True)
    duration = models.IntegerField(default=45, verbose_name=_('duration'))
    timetable_version = models.ForeignKey(TimetableVersion, related_name='cards')


class Term(models.Model):
    datetime = models.DateTimeField(verbose_name=_('date'))
    card = models.ForeignKey(Card, related_name='terms')
    lesson = models.OneToOneField(Lesson, blank=True, verbose_name=_('lesson'))
    duration = models.IntegerField(default=45, verbose_name=_('duration'))


