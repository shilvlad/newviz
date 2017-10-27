# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 13:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0017_act_printer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Printer',
            new_name='Device',
        ),
        migrations.RenameModel(
            old_name='RelCartridgePrinter',
            new_name='RelDeviceSupply',
        ),
        migrations.RenameModel(
            old_name='Cartridge',
            new_name='Supply',
        ),
        migrations.RenameField(
            model_name='act',
            old_name='Printer',
            new_name='Device',
        ),
        migrations.RenameField(
            model_name='act',
            old_name='Cartridge',
            new_name='Supply',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='PrinterName',
            new_name='DeviceName',
        ),
        migrations.RenameField(
            model_name='reldevicesupply',
            old_name='IdPrinter',
            new_name='Device',
        ),
        migrations.RenameField(
            model_name='reldevicesupply',
            old_name='IdCartridge',
            new_name='Supply',
        ),
    ]