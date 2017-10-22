# -*- coding: utf-8 -*-
from django import forms
from viz.models import Building, Cartridge, Printer, RelCartridgePrinter
from django.contrib.auth import authenticate


class ActForm(forms.Form):
    TaskId = forms.CharField(
        max_length=100,
        label=u'Номер задачи',
        widget=forms.TextInput(attrs={'class': 'TaskID', 'placeholder': 'TAS000XXXXXXXXXX', 'name': 'TaskID'}),
        error_messages={'required': u'Обязательное поле!'}
    )
    BarCode = forms.CharField(
        max_length=100,
        label=u'Баркод',
        widget=forms.TextInput(attrs={'class': 'Barcode', 'placeholder': 'XXX-XXXXXX', 'name': 'Barcode'}),
        error_messages={'required': u'Обязательное поле!'}
    )
    UserName = forms.CharField(
        max_length=100,
        label=u'Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'afluser', 'placeholder': u'ФИО пользователя', 'name': 'afluser'}),
        error_messages={'required': u'Обязательное поле!'}
    )
    Building = forms.ModelChoiceField(Building.objects.all())
    Location = forms.CharField(
        max_length=100,
        label=u'Местоположение',
        widget=forms.TextInput(attrs={'class': 'Barcode', 'placeholder': u'Кабинет', 'name': 'Location'}),
        error_messages={'required': u'Обязательное поле!'}
    )

    Printer = forms.ModelChoiceField(Printer.objects.all())
    Cartridge = forms.ModelChoiceField(Cartridge.objects.all())
    Specialist = forms.CharField(
        max_length=100,
        label=u'Специалист',
        widget=forms.TextInput(attrs={'class': 'Barcode', 'placeholder': u'ФИО Специалиста', 'name': 'Location'}),
        error_messages={'required': u'Обязательное поле!'}
    )



