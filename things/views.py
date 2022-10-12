from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = HttpResponse("Welcome to thingproject")
    return response

def secondpage(request):
    return render(request, 'home.html')