# -*- coding: UTF-8 -*-

"""
File Name:      urls
Author:         zhangwei04
Create Date:    2019/2/2
"""

from django.urls import path

from . import views


app_name = 'pingback'

urlpatterns = [
    path('', views.index),
    path('disk/', views.register),
]
