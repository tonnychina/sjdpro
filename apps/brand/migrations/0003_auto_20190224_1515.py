# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-24 15:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brand', '0002_userbrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.ImageField(help_text='二维码图片', upload_to='code/', verbose_name='二维码图片')),
                ('banner', models.ImageField(help_text='轮播图', upload_to='banner/', verbose_name='轮播图')),
                ('name', models.CharField(default='', help_text='门店名称', max_length=255, verbose_name='门店名称')),
                ('address', models.CharField(default='', help_text='地址', max_length=255, verbose_name='地址')),
                ('location_x', models.FloatField(default='', help_text='位置经度', verbose_name='位置经度')),
                ('location_y', models.FloatField(default='', help_text='位置纬度', verbose_name='位置纬度')),
                ('contact', models.CharField(default='', help_text='联系方式', max_length=255, verbose_name='联系方式')),
                ('info', models.TextField(default='', help_text='机构介绍', verbose_name='机构介绍')),
                ('cate', models.ForeignKey(blank=True, help_text='分类id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_sub', to='brand.BrandCate', verbose_name='分类id')),
                ('user', models.ForeignKey(blank=True, help_text='用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_sub', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '店铺',
                'verbose_name_plural': '店铺',
            },
        ),
        migrations.RemoveField(
            model_name='userbrand',
            name='bcate',
        ),
        migrations.DeleteModel(
            name='UserBrand',
        ),
    ]
