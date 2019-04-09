from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.views import generic
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse, JsonResponse
from .models import User
import os


def index(request):
    try:
        return render(request, 'pingback/index.html', {"a":None})
    except Exception as e:
        print(e)
    return None


class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()


def upload(request):
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


def upload_file(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist("file")
        try:
            for file in uploaded_files:
                filename = file.name
                _handle_uploaded_file(os.path.join("pingback", "upload_files", filename), file)
                result_json = {'method': 'post'}
        except Exception as e:
            result_json = {"msg": str(e)}
        result = {
            'error': result_json
        }
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({"error": "method is not post"})


def _handle_uploaded_file(filename, f):
    try:
        destination = open(filename, 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
    except Exception as e:
        raise Exception('save %s failed: %s' % (filename, str(e)))
