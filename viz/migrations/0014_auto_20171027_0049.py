# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-26 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0013_auto_20171027_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstories',
            name='Author',
            field=models.CharField(max_length=100),
        ),
    ]