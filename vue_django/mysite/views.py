from django.template import Template
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse
from django.http import HttpRequest


# Create your views here.

def index(request):
    for i in range( 1, 5, 1 ):
        url = requests.get(f'https://www.drogasil.com.br/medicamentos.html?p={i}')
        soup = BeautifulSoup( url.content, 'html.parser' )
        medicamento = (soup.find_all('a', class_='LinkNextstyles__LinkNextStyles-t73o01-0 cpRdBZ LinkNext'))
        return render(request, 'polls/index.html', {'medicamento': medicamento})



def contato(request):
    return render(request, 'polls/contato.html')



