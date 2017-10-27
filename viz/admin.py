from django.contrib import admin
from models import Supply, Building, Device, RelDeviceSupply, UserStory, Act

# Register your models here.
admin.site.register(Supply)
admin.site.register(Building)
admin.site.register(Device)
admin.site.register(RelDeviceSupply)
admin.site.register(Act)
admin.site.register(UserStory)