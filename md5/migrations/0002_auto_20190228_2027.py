# Generated by Django 2.1.4 on 2019-02-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('md5', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encryptedrecord',
            name='text',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='encryptedrecord',
            name='encry_text',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
