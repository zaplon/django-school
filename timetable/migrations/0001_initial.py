# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField(blank=True, null=True, verbose_name='day of week')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='hour')),
                ('duration', models.IntegerField(default=45, verbose_name='duration')),
                ('students', models.ManyToManyField(related_name='terms', to='account.Student', verbose_name='students')),
                ('teachers', models.ManyToManyField(related_name='terms', to='account.Teacher', verbose_name='teachers')),
            ],
            options={
                'verbose_name': 'Card',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=256, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='subject.Subject')),
            ],
            options={
                'verbose_name': 'Lesson',
            },
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('excused', 'excused')], max_length=16, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Presence',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='date')),
                ('duration', models.IntegerField(default=45, verbose_name='duration')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terms', to='timetable.Card')),
                ('lesson', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.Lesson', verbose_name='lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Timetable',
            },
        ),
        migrations.CreateModel(
            name='TimetableVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='timetable.Timetable')),
            ],
            options={
                'get_latest_by': 'number',
            },
        ),
        migrations.CreateModel(
            name='StudentPresence',
            fields=[
                ('presence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='timetable.Presence')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Student')),
            ],
            bases=('timetable.presence',),
        ),
        migrations.CreateModel(
            name='TeacherPresence',
            fields=[
                ('presence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='timetable.Presence')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Teacher')),
            ],
            bases=('timetable.presence',),
        ),
        migrations.AddField(
            model_name='presence',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presences', to='timetable.Lesson'),
        ),
        migrations.AddField(
            model_name='card',
            name='timetable_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='timetable.TimetableVersion'),
        ),
    ]