from urllib import request

from django.urls import path
from . import views
from django.contrib import admin

app_name = 'mysite'

urlpatterns = [

    path('', views.index, name='index'),
    path('', views.contato, name='contato')

]
