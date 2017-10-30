# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Supply, Building, Device, RelDeviceSupply, UserStory, Act, Department, SupplyType

# Register your models here.
admin.site.register(Supply)
admin.site.register(Building)
admin.site.register(Device)
admin.site.register(RelDeviceSupply)
admin.site.register(Act)
admin.site.register(UserStory)
admin.site.register(Department)
admin.site.register(SupplyType)