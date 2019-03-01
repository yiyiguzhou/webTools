# -*- coding: UTF-8 -*-

"""
File Name:      urls
Author:         zhangwei04
Create Date:    2019/2/2
"""

from django.urls import path

from . import views


app_name = 'md5'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('encrypt/', views.Encrypt.as_view(), name='encrypt_main'),
    path('encrypt_method/', views.encrypt_method, name='encrypt_method'),
    path('encrypt_result/<str:pk>', views.encrypt_result, name='encrypt_result'),
]
