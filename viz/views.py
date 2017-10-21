from django.shortcuts import render

def start(request):
#    return render(request, 'main.html', {'username':request.user.username})
    return render(request, 'main.html')