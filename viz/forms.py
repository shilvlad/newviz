# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from viz.models import Building, Supply, Device, RelDeviceSupply, UserStory
from models import UserStory, Act
from django.contrib.auth import authenticate


class ActForm(forms.Form):
    TaskId = forms.CharField(
        max_length=100,
        label=u'Номер задачи',
        widget=forms.TextInput(attrs={'class': 'TaskID', 'placeholder': 'TAS000XXXXXXXXXX', 'name': 'TaskID'}),
        error_messages={'required': u'Обязательное поле!'},
    )

    def as_td(self):
        return self._html_output(
            normal_row=u'<tr><td%(html_class_attr)s>%(label)s </td><td>%(field)s %(help_text)s %(errors)s</td></tr>',
            error_row=u'<td class="error">%s</td>',
            row_ender='</tr>',
            help_text_html=u'<div class="hefp-text">%s</div>',
            errors_on_separate_row=False)

# Добавление User Story
class ModelActForm(ModelForm):
    class Meta:
        model = Act
        fields = '__all__'
        labels = {
            "TaskId":"Номер задачи",
            "BarCode":"Баркод устройства",
            "UserName":"ФИО пользователя",
            "IdBuilding":"Здание",
            "Location":"Расположение",
            "Device":"Устройство",
            "Supply":"Расходник",
            "Specialist":"Сотрудник",
        }

class ModelCreateUS(ModelForm):
    class Meta:
        model = UserStory
        fields = {'FullDescription', 'ShortDescription'}
        labels = {
            "ShortDescription": "Краткое описание",
            "FullDescription": "Подробности",
        }
    def as_oc(self):
        return self._html_output(
            normal_row=u'<p%(html_class_attr)s>%(label)s </p><p>%(field)s %(help_text)s %(errors)s</p>',
            error_row=u'<div class="error">%s</div>',
            row_ender='</p>',
            help_text_html=u'<div class="hefp-text">%s</div>',
            errors_on_separate_row=False)
