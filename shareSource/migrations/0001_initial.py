# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('ddl', models.DateField()),
                ('reference', models.CharField(max_length=30)),
                ('courseid', models.CharField(max_length=15)),
                ('comment', models.FileField(upload_to='uploads/assignment/')),
            ],
        ),
        migrations.CreateModel(
            name='assignment_store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignmentid', models.CharField(max_length=15)),
                ('studentid', models.CharField(max_length=15)),
                ('file_name', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=20)),
                ('file_id', models.IntegerField()),
                ('user_id', models.IntegerField(default=0)),
                ('file_name', models.CharField(max_length=40)),
                ('file_path', models.FileField(upload_to='uploads/assignment/')),
                ('update_time', models.DateTimeField()),
                ('download_times', models.IntegerField()),
                ('flag', models.IntegerField()),
                ('flag_top', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('sectionid', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('s', 'student'), ('t', 'teacher'), ('m', 'manager')], max_length=1)),
            ],
        ),
    ]
