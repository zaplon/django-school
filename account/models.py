from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class Student(models.Model):
    class Meta:
        verbose_name = _('Student')
    user = models.OneToOneField(User)


class Teacher(models.Model):
    class Meta:
        verbose_name = _('Teacher')
    user = models.OneToOneField(User)


class Employee(models.Model):
    class Meta:
        verbose_name = _('Employee')
    user = models.OneToOneField(User)
