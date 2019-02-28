import datetime

from django.db import models
from django.utils import timezone


class EncryptedRecord(models.Model):
    encry_date = models.DateTimeField('date encrypted')
    encry_text = models.CharField(max_length=1000, default='')
    text = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.encry_text