# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-28 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0022_auto_20171028_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='Supply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viz.SupplyType'),
        ),
    ]