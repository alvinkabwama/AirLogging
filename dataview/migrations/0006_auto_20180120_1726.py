# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-20 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataview', '0005_auto_20180120_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='co2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='data',
            name='pm25',
            field=models.CharField(max_length=255),
        ),
    ]
