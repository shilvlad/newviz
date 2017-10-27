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
    Device = models.ForeignKey('Device')
    Supply = models.ForeignKey('Supply')
    Specialist = models.CharField(max_length=100)
    def __str__(self):
        return self.TaskId

class Building(models.Model):
    BuildingName = models.CharField(max_length=100)
    def __str__(self):
        return self.BuildingName.encode('utf-8')

class Supply(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.Name.encode('utf-8')

class Device(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.Name.encode('utf-8')

class RelDeviceSupply(models.Model):
    Device = models.ForeignKey('Device')
    Supply = models.ForeignKey('Supply')
    def __str__(self):
        return self.Device.Name.encode('utf-8') + ' - ' + self.Supply.Name.encode('utf-8')

class UserStory(models.Model):
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