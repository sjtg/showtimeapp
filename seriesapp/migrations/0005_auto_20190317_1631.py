# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-17 16:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seriesapp', '0004_auto_20190317_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('publishedDate', models.IntegerField(blank=True, null=True)),
                ('seriesImages', models.FileField(null=True, upload_to=b'Series/SeriesImage/')),
                ('episodes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seriesapp.Episodes')),
                ('genres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seriesapp.Genre')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='series',
            name='seasons',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seriesapp.Seasons'),
            preserve_default=False,
        ),
    ]
