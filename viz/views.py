# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.shortcuts import HttpResponseRedirect, HttpResponse
from forms import ActForm, ModelCreateUS, ModelActForm
from models import Act
from datetime import datetime, date, time
from models import SupplyType, Supply





def start(request):


    return render(request, 'viz/main.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponseRedirect('/')
    else:
        return HttpResponse("Херня какая-то")

def user_logout(request):
    logout(request)
    return render(request, 'viz/main.html')

def createus(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ModelCreateUS(request.POST)
            if form.is_valid():
                form.save()

                return render(request, 'viz/createussuccess.html')
            else:
                return HttpResponse("Форма не валидна")
        else:
            form = ModelCreateUS()
            return render(request, 'viz/createus.html', {'form': form})
    else:
        return HttpResponse("Залогинься!")

def createact(request):
    if request.method == 'POST':
        print "Проверяем форму акта"
        form = ModelActForm(request.POST)
        if form.is_valid():
            print "Форма акта валидна"
            f = form.save()
            date = datetime.now()
            s = SupplyType.objects.get(Name=form.cleaned_data['Supply'])
            print s.Name
            #st = SupplyType.objects.get()

            context = {
                'date': date.strftime("%d-%m-%Y"),
                'barcode': form.cleaned_data['BarCode'],
                'device': form.cleaned_data['Device'],
                'building': form.cleaned_data['IdBuilding'],
                'location': form.cleaned_data['Location'],
                'department': form.cleaned_data['Department'],
                'taskid': form.cleaned_data['TaskId'],
                'supply': form.cleaned_data['Supply'],
                'user': form.cleaned_data['UserName'],
                'specialist': form.cleaned_data['Specialist'],
                'supplytype': st.Name.encode('urf-8')
            }

            return render(request, 'viz/createactsuccess.html', context)
    else:
        form = ModelActForm(initial={'Specialist': request.user.id})


    return render(request, 'viz/createact.html', {'form': form})
