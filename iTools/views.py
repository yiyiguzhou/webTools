# -*- coding: UTF-8 -*-
"""
File Name:      views
Author:         wzhang
Create Date:    11/26/18
"""
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")