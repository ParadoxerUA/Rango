from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    path = request.path
    return HttpResponse('<a href="/rango/about/">About</a>')

def about(request):
    return HttpResponse("Rango says here is the about page.")

