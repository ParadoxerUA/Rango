from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "My Tamplate, embedding python vars \
		            in html is easy "}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse('<p>about rango...</p>'
                        '<a href="/rango/">Back</a>')

