# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-27 15:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0011_auto_20190227_1456'),
        ('resoucedit', '0002_auto_20190226_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandCateImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='名称', max_length=255, verbose_name='名称')),
                ('image', models.ImageField(help_text='描述', upload_to='brandimage/%Y/%m/%d/', verbose_name='描述')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
                ('cate', models.ForeignKey(blank=True, help_text='分类id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_images', to='brand.BrandCate', verbose_name='分类id')),
            ],
            options={
                'verbose_name': '行业图片',
                'verbose_name_plural': '行业图片',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='名称', max_length=255, verbose_name='名称')),
                ('desc', models.CharField(default='', help_text='描述', max_length=255, verbose_name='描述')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '行业标题',
                'verbose_name_plural': '行业标题',
            },
        ),
    ]
