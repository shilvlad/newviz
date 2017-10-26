# -*- coding: utf-8 -*-
from django import forms
from viz.models import Building, Cartridge, Printer, RelCartridgePrinter
from django.contrib.auth import authenticate


class ActForm(forms.Form):
    TaskId = forms.CharField(
        max_length=100,
        label=u'Номер задачи',
        widget=forms.TextInput(attrs={'class': 'TaskID', 'placeholder': 'TAS000XXXXXXXXXX', 'name': 'TaskID'}),
        error_messages={'required': u'Обязательное поле!'},
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
    def as_td(self):
        return self._html_output(
            normal_row=u'<tr><td%(html_class_attr)s>%(label)s </td><td>%(field)s %(help_text)s %(errors)s</td></tr>',
            error_row=u'<td class="error">%s</td>',
            row_ender='</tr>',
            help_text_html=u'<div class="hefp-text">%s</div>',
            errors_on_separate_row=False)

# Добавление User Story
class CreateUS(forms.Form):
    ShortDesc = forms.CharField(
        widget=forms.TextInput(attrs={'size': '99', 'class': 'ShortDesc', 'name': 'ShortDesc'}),
        label = u'Краткое описание',
    )
    FullDesc = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 100, 'rows': 20 }),
        label=u'Подробное описание',
    )
    def as_oc(self):
        return self._html_output(
            normal_row=u'<p%(html_class_attr)s>%(label)s </p><p>%(field)s %(help_text)s %(errors)s</p>',
            error_row=u'<div class="error">%s</div>',
            row_ender='</p>',
            help_text_html=u'<div class="hefp-text">%s</div>',
            errors_on_separate_row=False)

