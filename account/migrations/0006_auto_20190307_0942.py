# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-07 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_customuser_profileimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='decodertype',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='iucnumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profileImages',
            field=models.FileField(blank=True, null=True, upload_to=b'Profile/ProfileImage/'),
        ),
    ]
