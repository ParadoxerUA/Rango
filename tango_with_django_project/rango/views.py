from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    path = request.path
    return HttpResponse('<p>you are on the home page</p>'
                        '<a href="/rango/about/">About</a>')

def about(request):
    return HttpResponse('<p>about rango...</p>'
                        '<a href="/rango/">Back</a>')

