# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacci_app', '0002_auto_20180404_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historydata',
            name='fibonacci_result',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
