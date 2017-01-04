from __future__ import unicode_literals

from django.db import models

# Create your models here.

sectors=(
    ('IT','IT'),
    ('DEVELOPER','developer'),
    ('TESTER','tester')
)

class Recruiter(models.Model):
    recruiter = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    salary = models.IntegerField()
    location = models.CharField(max_length=30)
    sector = models.CharField(max_length=30,choices=sectors)
    job_type = models.CharField(max_length=20)
    contact = models.TextField(max_length=100)

class user_rights(models.Model):
    user_id = models.IntegerField(max_length=2)
    type = models.IntegerField(max_length = 1)

class employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    got_job = models.BooleanField(default=False)

class job_user_map(models.Model):
    employee_id = models.ForeignKey(
        employee,
        on_delete=models.CASCADE
    )
    job_id = models.IntegerField(max_length=10)

class search(models.Model):
    location = models.CharField(max_length=30)
    sector = models.CharField(choices=sectors,max_length=30)
    salary_range = models.IntegerField(max_length=7)