# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-13 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_auto_20170223_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votestatus',
            name='has_voted',
            field=models.BooleanField(default=False, verbose_name='Has Voted'),
        ),
    ]