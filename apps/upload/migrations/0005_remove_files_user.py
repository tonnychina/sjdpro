# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-26 15:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_files_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='user',
        ),
    ]