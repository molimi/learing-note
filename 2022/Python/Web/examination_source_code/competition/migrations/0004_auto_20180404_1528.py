# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-04 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0003_auto_20180401_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitionqainfo',
            name='score',
            field=models.FloatField(default=0, help_text='分数', verbose_name='得分'),
        ),
    ]
