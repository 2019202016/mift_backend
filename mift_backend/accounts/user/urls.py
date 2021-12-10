#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:04:16 2019

"""
from django.conf.urls import url
from mift_backend.accounts.user.views import UserRegistrationView
from mift_backend.accounts.user.views import UserLoginView

urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', UserLoginView.as_view(), name="sign_in"),
    ]
