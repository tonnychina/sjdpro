# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-26 13:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20190226_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='addtime',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
    ]
