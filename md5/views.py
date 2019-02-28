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
    model = EncryptedRecord
    template_name = 'md5/encrypt.html'


def encrypt(request):
    encrypt_record = get_object_or_404(EncryptedRecord)
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if text:
            try:
                encrypt_line = encrypt_record.get(text=text)
            except:
                encrypt_text = base64.encodebytes(bytes(text))
                encrypt_line = EncryptedRecord.objects.create(encry_date=timezone.now(), encry_text=encrypt_text, text=text)
            return render(request, 'md5/encrypt.html', {
                'encrypt_line': encrypt_line,
                'error_message': "encrypt page error",
            })
    return render(request, 'md5/index.html')
