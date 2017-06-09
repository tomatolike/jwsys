from django.db import models
from django.contrib.auth.models import User
from courseArrange.models import *


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    building = models.CharField(max_length=100)


class Major(models.Model):
    name = models.CharField(max_length=50, default='', unique=True)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_file = models.ImageField(upload_to='images/')
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    gender = models.IntegerField()


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_file = models.ImageField(upload_to='images/')
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    gender = models.IntegerField()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_file = models.ImageField(upload_to='images/')
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    tot_cred = models.IntegerField(default=0)
    major = models.ForeignKey(Major, null=True, on_delete=models.SET_NULL)
    matriculate = models.IntegerField()
    graduate = models.IntegerField(null=True)
    gender = models.IntegerField()


class Course(models.Model):
    course_number = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    credits = models.IntegerField()
    week_hour = models.IntegerField()
    type = models.CharField(max_length=20)
    precourse = models.ForeignKey('Course', null=True, on_delete=models.SET_NULL)
    method=models.CharField(max_length=30)


class Log(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    event = models.TextField()


class Classroom(models.Model):
    building = models.CharField(max_length=100)
    room_number = models.IntegerField()
    capacity = models.IntegerField()
    equipment = models.ManyToManyField('Equipment')

    class Meta:
        unique_together = ('building', 'room_number')


class TimeSlot(models.Model):
    day = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('day', 'start_time', 'end_time')


class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Takes(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    score = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
