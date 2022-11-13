from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import info
from myapp.models import info

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
def busqueda_residuos(request):
    return render(request, "busqueda_residuos.html")    
def buscar(request):
    if request.GET["residuo"]:
        mensaje="Residuo buscado: %r" %request.GET["residuo"]
        residuo_ingresado=request.GET["residuo"]
        if residuo_ingresado == "Plástico":
            residuos_buscados=info.objects.filter(residuos__icontains= 1)
        elif residuo_ingresado == "Latas":
            residuos_buscados=info.objects.filter(residuos__icontains=2)
        elif residuo_ingresado == "Residuos Orgánicos":
            residuos_buscados=info.objects.filter(residuos__icontains=3)
        elif residuo_ingresado == "Residuos Metálicos":
            residuos_buscados=info.objects.filter(residuos__icontains=4)
        elif residuo_ingresado == "Ropa/Tela":
            residuos_buscados=info.objects.filter(residuos__icontains=5)
        elif residuo_ingresado == "Carton":
            residuos_buscados=info.objects.filter(residuos__icontains=6)
        elif residuo_ingresado == "Vidrios":
            residuos_buscados=info.objects.filter(residuos__icontains=7)
        elif residuo_ingresado == "Madera":
            residuos_buscados=info.objects.filter(residuos__icontains=8)
        elif residuo_ingresado == "Papel":
            residuos_buscados=info.objects.filter(residuos__icontains=9)
        elif residuo_ingresado == "Baterias y pilas":
            residuos_buscados=info.objects.filter(residuos__icontains=10)
        elif residuo_ingresado == "Chatarra":
            residuos_buscados=info.objects.filter(residuos__icontains=11)
        else:
            residuos_buscados=info.objects.filter(residuos__icontains=12)
    return render(request, "resultados_busqueda.html", {"residuos_buscados":residuos_buscados, "query":residuo_ingresado})
