from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    # return HttpResponse('Hello There, Friend')
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters = [random.choice([i.upper(), i]) for i in characters]
        # characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('numbers'):
        characters += list('1234567890')

    if request.GET.get('special'):
        characters += list('!@#$%^&*')

    password_name = ''
    for i in range(length):
        password_name += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password_name})


def about(request):
    return render(request, 'generator/about.html')
