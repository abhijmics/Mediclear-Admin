# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class idcard(models.Model):
    name = models.CharField(max_length=200,null=True)
    employment_id = models.CharField(max_length=200,null=True)
    customer_account_no = models.CharField(max_length=200,null=True)
    circle = models.CharField(max_length=200,null=True)
    company_name = models.CharField(max_length=200,null=True)
    department = models.CharField(max_length=200,null=True)
    certificate_no = models.CharField(max_length=200,null=True)
    date = models.CharField(max_length=200,null=True)
    objects=models.Manager()
    def __str__(self):
        return self.name

    
    
class Certificate(models.Model):
    #serial_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=120,null=True)
    training_name=models.CharField(max_length=120,null=True)
    certificate_validity = models.CharField(max_length=120,null=True)
    date = models.CharField(max_length=120,null=True)
    place = models.CharField(max_length=120,null=True)
    objects=models.Manager()
     

    def __str__(self):
        return self.name

class Report(models.Model):
    name=models.CharField(max_length=120,null=True,blank=True)
    gender=models.CharField(max_length=120,null=True,blank=True)
    address=models.CharField(max_length=120,null=True,blank=True)
    dob=models.CharField(max_length=120,null=True,blank=True)
    email=models.CharField(max_length=120,null=True,blank=True)
    q_choices=[
        ('Yes','Yes'),
        ('No','No'),
    ]
    q1=models.CharField(max_length=120,null=True,choices=q_choices,blank=True)
    q2=models.CharField(max_length=120,null=True,choices=q_choices,blank=True)
    q3=models.CharField(max_length=120,null=True,choices=q_choices,blank=True)
    q4=models.CharField(max_length=120,null=True,choices=q_choices,blank=True)
    q5=models.CharField(max_length=120,null=True,choices=q_choices,blank=True)
    q6=models.CharField(max_length=120,null=True,choices=q_choices,blank=True)
    q7=models.CharField(max_length=120,null=True,choices=q_choices,blank=True)
    q8=models.CharField(max_length=120,null=True,choices=q_choices,blank=True)
    q9=models.CharField(max_length=120,null=True,choices=q_choices,blank=True)
    q10=models.CharField(max_length=120,null=True,choices=q_choices,blank=True)
    q11=models.CharField(max_length=120,null=True,choices=q_choices,blank=True)
    comment=models.CharField(max_length=120,null=True,blank=True)
    image=models.ImageField( upload_to="profiles", height_field=None, width_field=None, max_length=None,null=True)
    comment=models.CharField(max_length=120,null=True,blank=True)
    height=models.CharField(max_length=120,null=True,blank=True)
    weight=models.CharField(max_length=120,null=True,blank=True)
    systolic=models.CharField(max_length=120,null=True,blank=True)
    diastolic=models.CharField(max_length=120,null=True,blank=True)
    pulserate=models.CharField(max_length=120,null=True,blank=True)
    heartsound=models.CharField(max_length=120,null=True,blank=True)
    peripheralpulse=models.CharField(max_length=120,null=True,blank=True)
    chestlung=models.CharField(max_length=120,null=True,blank=True)
    curvicalspine=models.CharField(max_length=120,null=True,blank=True)
    backmovements=models.CharField(max_length=120,null=True,blank=True)
    upperlimbs=models.CharField(max_length=120,null=True,blank=True)
    jointmovements=models.CharField(max_length=120,null=True,blank=True)
    reflexes=models.CharField(max_length=120,null=True,blank=True)
    rombergs=models.CharField(max_length=120,null=True,blank=True)
    hearing=models.CharField(max_length=120,null=True,blank=True)
    vision=models.CharField(max_length=120,null=True,blank=True)
    albumin=models.CharField(max_length=120,null=True,blank=True)
    sugar=models.CharField(max_length=120,null=True,blank=True)
    blood_group=models.CharField(max_length=120,null=True,blank=True)
    rh_factor=models.CharField(max_length=120,null=True,blank=True)
    hb=models.CharField(max_length=120,null=True,blank=True)
    tlc=models.CharField(max_length=120,null=True,blank=True)
    rbc=models.CharField(max_length=120,null=True,blank=True)
    plateletscount=models.CharField(max_length=120,null=True,blank=True)
    triglycerides=models.CharField(max_length=120,null=True,blank=True)
    hdl=models.CharField(max_length=120,null=True,blank=True)
    ldl=models.CharField(max_length=120,null=True,blank=True)
    result=models.CharField(max_length=120,null=True,blank=True)
    comment=models.CharField(max_length=120,null=True,blank=True)
    registration_no=models.CharField(max_length=120,null=True,blank=True)
    date_of_examination=models.CharField(max_length=120,null=True,blank=True)
    objects=models.Manager()

    def __str__(self):
        return self.name

