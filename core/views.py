#from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def teste(request):
    return HttpResponse('Olá mundo do Django.')

def teste2(request):
    return HttpResponse('Uma nova página.')