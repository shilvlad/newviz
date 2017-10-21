from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Acts(models.Model):
    TaskId = models.CharField(max_length=100)
    BarCode = models.CharField(max_length=10)
    UserName = models.CharField(max_length=100)
    IdBuilding = models.ForeignKey('Buildings')
    Location = models.CharField(max_length=100)
    DateTime = models.DateTimeField
    Cartridge = models.ForeignKey('Cartridges')
    Specialist = models.CharField(max_length=100)
    def __str__(self):
        return self.TaskId

class Buildings(models.Model):
    BuildingName = models.CharField(max_length=100)
    def __str__(self):
        return self.BuildingName

class Cartridges(models.Model):
    CartridgeName = models.CharField(max_length=100)
    Description = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.CartridgeName

class Printers(models.Model):
    PrinterName = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    def __str__(self):
        return self.PrinterName


