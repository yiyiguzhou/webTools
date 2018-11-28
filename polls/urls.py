# -*- coding: UTF-8 -*-
"""
File Name:      urls
Author:         wzhang
Create Date:    11/27/18
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]