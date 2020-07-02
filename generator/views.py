from django.shortcuts import render
from django.http import HttpResponse
import random
# Views of every webpage are defined here

#View of Home page
def home(request):
    #render function gives a HttpResponse of the mentioned webpage in the path
    return render(request, 'generator/home.html')

#View of About Us page
def about(request):
    return render(request, 'generator/about.html')

#View of Password page
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    #To-do when the user checks one or more parameters to customize the password.
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special_char'):
        characters.extend(list('!@#$%^&*-_'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    #converting the length response to an integer
    length = int(request.GET.get('length', 10))
    
    generated_password = ''
    
    #generating the password using random function & length as an input range
    for x in range(length):
        generated_password += random.choice(characters)
        x += 1

    return render(request, 'generator/password.html', {'password': generated_password})