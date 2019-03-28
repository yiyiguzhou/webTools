from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.views import generic
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from .models import User


def index(request):
    try:
        return render(request, 'pingback/index.html', {"a":None})
    except Exception as e:
        print(e)
    return None


class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()


def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            # 获取表单信息
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            # 写入数据库
            user = User()
            try:
                user.username = username
                user.headImg = headImg
                user.save()
            except Exception as e:
                print(e)
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    try:
        return render_to_response('pingback/register.html', {'uf': uf})
    except Exception as e:
        print(e)
        return None
