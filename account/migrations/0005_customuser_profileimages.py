# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190224_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profileImages',
            field=models.FileField(null=True, upload_to=b'Profile/ProfileImage/'),
        ),
    ]