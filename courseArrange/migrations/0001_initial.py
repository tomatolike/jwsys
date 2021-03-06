# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basicInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCandiate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('classroom_type', models.IntegerField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basicInfo.Course')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basicInfo.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='InstructorBusyTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('start_time', models.IntegerField()),
                ('end_time', models.IntegerField()),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basicInfo.Instructor')),
                ('time_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basicInfo.TimeSlot')),
            ],
        ),
        migrations.CreateModel(
            name='Prereq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allPreCourses', to='basicInfo.Course')),
                ('precourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subCourses', to='basicInfo.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SecTimeClassroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basicInfo.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('max_number', models.IntegerField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basicInfo.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basicInfo.Instructor')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courseArrange.Section')),
            ],
        ),
        migrations.AddField(
            model_name='sectimeclassroom',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courseArrange.Section'),
        ),
        migrations.AddField(
            model_name='sectimeclassroom',
            name='time_slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basicInfo.TimeSlot'),
        ),
    ]
