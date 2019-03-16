# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-26 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0008_auto_20190225_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='banner',
            field=models.ImageField(blank=True, help_text='轮播图', null=True, upload_to='uploads/banner/%Y/%m/%d/', verbose_name='轮播图'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='code',
            field=models.ImageField(blank=True, help_text='二维码图片', null=True, upload_to='uploads/code/%Y/%m/%d/', verbose_name='二维码图片'),
        ),
    ]
