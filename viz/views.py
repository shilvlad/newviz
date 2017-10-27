# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.shortcuts import HttpResponseRedirect, HttpResponse
from forms import ActForm, ModelCreateUS, ModelActForm
from models import UserStory






def start(request):


    return render(request, 'viz/main.html')

def createact(request):
    if request.method == 'POST':
        print "Проверяем форму акта"
        form = ModelActForm(request.POST)
        if form.is_valid():
            print "Форма акта валидна"
            form.save()
            return HttpResponseRedirect('/createactsuccess/', {'form': form})
    else:
        form = ModelActForm()
    return render(request, 'viz/createact.html', {'form': form})

def createactsuccess(request):

    return render(request, 'viz/createactsuccess.html')

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


                return HttpResponse("Чудненько")
            else:
                return HttpResponse("Форма не валидна")
        else:
            form = ModelCreateUS()
            return render(request, 'viz/createus.html', {'form': form})
    else:
        return HttpResponse("Залогинься!")

