# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 23:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_auto_20160731_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='graduation_year',
        ),
        migrations.AddField(
            model_name='user',
            name='graduation_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 31, 23, 58, 56, 340561, tzinfo=utc),
                                   verbose_name='Graduation Date'),
            preserve_default=False,
        ),
    ]
