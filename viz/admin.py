from django.contrib import admin
from models import Cartridge, Building, Printer, RelCartridgePrinter

# Register your models here.
admin.site.register(Cartridge)
admin.site.register(Building)
admin.site.register(Printer)
admin.site.register(RelCartridgePrinter)
