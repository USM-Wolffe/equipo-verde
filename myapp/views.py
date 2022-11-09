from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import info
# Create your views here.

def index(request):
    return HttpResponse("Index page")
def hello(request):
    return HttpResponse("Hello world")
def about(request):
    return HttpResponse("sobre nosotros")
def registro(request):
    informacion= list(info.objects.values())
    return JsonResponse(informacion, safe=False)
def perfil(request):
    return HttpResponse("Perfil")
def myspace(request):
    return HttpResponse("myspace")
    
    
