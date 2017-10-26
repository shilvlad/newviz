# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.shortcuts import HttpResponseRedirect, HttpResponse
from forms import ActForm, CreateUS
from models import UserStories



# TODO Дописываем в части создания акта
# FIXME Не создается акт
#
def start(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        # check whether it's valid:
        if form.is_valid():

            return HttpResponseRedirect('/thanks/')

    else:
        form = ActForm()

    return render(request, 'main.html', {'form': form})



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
    return render(request, 'main.html')

def createus(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateUS(request.POST)
            if form.is_valid():

                print "Форма Валидна"
                UserStory = UserStories()
                UserStory.ShortDescription = request.POST['ShortDesc']
                UserStory.FullDescription = request.POST['FullDesc']
                UserStory.Author = request.user.username
                UserStory.save()
                return HttpResponse("Чудненько")
            else:
                return HttpResponse("Форма не валидна")
        else:
            form = CreateUS()
            return render(request, 'createus.html', {'form': form})
    else:
        return HttpResponse("Залогинься!")

