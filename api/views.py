from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def minhaView(request):
    return HttpResponse ( 'Minha View')
    
def sobreNos(request):
    return HttpResponse ('<h2> Sobre Nós <h2>')

def meusContatos(request):
    return HttpResponse ('Meus Contatos')

def raiz(request):
    return HttpResponse ('Raíz')