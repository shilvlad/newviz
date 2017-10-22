from django import forms
from viz.models import Building, Cartridge

class ActForm(forms.Form):
    TaskId = forms.CharField()
    BarCode = forms.CharField()
    UserName = forms.CharField()
    IdBuilding = forms.ModelChoiceField(Building.objects.all())
    Location = forms.CharField()
    DateTime = forms.DateTimeField
    Cartridge = forms.ModelChoiceField(Cartridge.objects.all())
    Specialist = forms.CharField()



