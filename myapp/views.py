from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Trabajador

def index(request):
    context = {}
    return render(request, 'index.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

def register(request):
    context = {}
    return render(request, 'register.html', context)

def buttons(request):
    context = {}
    return render(request, 'buttons.html', context)

def cards(request):
    context = {}
    return render(request, 'cards.html', context)

def charts(request):
    context = {}
    return render(request, 'charts.html', context)

def tables(request):
    context = {
        'trabajadores' : Trabajador.objects.all() 
    }
    return render(request, 'tables.html', context)

def utilities_color(request):
    context = {}
    return render(request, 'utilities-color.html', context)

def utilities_border(request):
    context = {}
    return render(request, 'utilities-border.html', context)

def utilities_animation(request):
    context = {}
    return render(request, 'utilities-animation.html', context)

def utilities_other(request):
    context = {}
    return render(request, 'utilities-other.html', context)

def forgot_password(request):
    context = {}
    return render(request, 'forgot-password.html', context)

def not_found(request):
    context = {}
    return render(request, '404.html', context)

def blank(request):
    context = {}
    return render(request, 'blank.html', context)






