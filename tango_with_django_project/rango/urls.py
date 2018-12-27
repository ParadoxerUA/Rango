from django.conf.urls import path
from rango import views

urlpatterns = [
    path(r'^$', views.index, name = 'index'),
]