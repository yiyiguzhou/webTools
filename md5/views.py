import base64
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import EncryptedRecord


class IndexView(generic.ListView):
    template_name = 'md5/index.html'
    context_object_name = 'latest_encrypt_list'

    def get_queryset(self):
        """Return the last five published questions."""
        a = EncryptedRecord.objects.all()[:]
        return a


class Encrypt(generic.DetailView):
    # model = EncryptedRecord
    template_name = 'md5/encrypt.html'
    context_object_name = "need_encrypt_list"

    def get_object(self, queryset=None):
        # try:
        #     a = get_object_or_404(EncryptedRecord, encry_date=timezone.now())
        # except:
        #     a = None
        return None


def encrypt_result(request, pk):
    if request.method == 'GET':
        encrypt_line = get_object_or_404(EncryptedRecord, text=pk)
        return render(request, 'md5/encrypt_result.html', {'encrypt_line': encrypt_line})
    else:
        return HttpResponseRedirect(reverse('md5:index.html', kwargs={'latest_encrypt_list': EncryptedRecord.objects.all()[:]}))


def encrypt_method(request):
    try:
        encrypt_record = EncryptedRecord.objects.all()
    except Exception as e:
        pass
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if text:
            try:
                encrypt_line = encrypt_record.get(text=text)
            except:
                try:
                    encrypt_text = base64.encodebytes(bytes(text, 'utf-8'))
                    encrypt_line = EncryptedRecord.objects.create(encry_date=timezone.now(), encry_text=encrypt_text, text=text)
                except Exception as e:
                    return HttpResponseRedirect(reverse('md5:', kwargs={'latest_encrypt_list': EncryptedRecord.objects.all()[:]}))
            return HttpResponseRedirect(reverse('md5:encrypt_result', args=(text,)))
    return HttpResponseRedirect(reverse('md5:index.html', kwargs={'latest_encrypt_list': EncryptedRecord.objects.all()[:]}))
