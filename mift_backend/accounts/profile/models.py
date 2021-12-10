#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:04:16 2019

@author: sambhav
"""

import uuid
from django.db import models
from mift_backend.accounts.user.models import User


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=10, unique=True, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    account_no = models.PositiveIntegerField(null=True, blank=True)
    ifsc = models.CharField(max_length=15, blank=True)
    account_holder_name = models.CharField(max_length=25, blank=True)
    address = models.TextField(max_length=50, blank=True)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile"
