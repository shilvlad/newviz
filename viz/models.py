from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Act(models.Model):
    TaskId = models.CharField(max_length=100)
    BarCode = models.CharField(max_length=10)
    UserName = models.CharField(max_length=100)
    IdBuilding = models.ForeignKey('Building')
    Location = models.CharField(max_length=100)
    DateTime = models.DateTimeField
    Cartridge = models.ForeignKey('Cartridge')
    Specialist = models.CharField(max_length=100)
    def __str__(self):
        return self.TaskId

class Building(models.Model):
    BuildingName = models.CharField(max_length=100)
    def __str__(self):
        return self.BuildingName.encode('utf-8')

class Cartridge(models.Model):
    CartridgeName = models.CharField(max_length=100)
    Description = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.CartridgeName.encode('utf-8')

class Printer(models.Model):
    PrinterName = models.CharField(max_length=100)
    Description = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.PrinterName.encode('utf-8')

class RelCartridgePrinter(models.Model):
    IdPrinter = models.ForeignKey('Printer')
    IdCartridge = models.ForeignKey('Cartridge')
    def __str__(self):
        return self.IdPrinter.PrinterName.encode('utf-8') + ' - ' + self.IdCartridge.CartridgeName.encode('utf-8')

class UserStories(models.Model):
    ShortDescription = models.CharField(max_length=100)
    FullDescription = models.TextField()
    CreateStamp = models.DateTimeField(auto_now_add=True)
    LastEditionStamp = models.DateTimeField(auto_now=True)
    Approved = models.BooleanField(editable=True, default=False)
    Solved = models.BooleanField(editable=True, default=False)
    Comment = models.TextField()
    Author = models.CharField(max_length=100)


    def __str__(self):
        return self.ShortDescription.encode('utf-8')