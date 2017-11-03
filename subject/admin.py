# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from subject.models import Subject, SubjectTemplate, TeacherEnrolment, StudentEnrolment


class TeachersInline(admin.TabularInline):
    model = TeacherEnrolment
    extra = 2


class StudentsInline(admin.TabularInline):
    model = StudentEnrolment
    extra = 2


class SubjectAdmin(admin.ModelAdmin):
    inlines = (TeachersInline, StudentsInline)


admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectTemplate)
