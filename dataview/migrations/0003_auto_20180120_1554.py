# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-20 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataview', '0002_auto_20180120_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dataview.Owner'),
        ),
    ]
