# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-21 22:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0005_auto_20171022_0124'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buildings',
            new_name='Building',
        ),
        migrations.RenameModel(
            old_name='Cartridges',
            new_name='Cartridge',
        ),
        migrations.RenameModel(
            old_name='Printers',
            new_name='Printer',
        ),
    ]