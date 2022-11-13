

from django.urls import URLPattern
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('registro/', views.registro),
    path('perfil/', views.perfil),
    path('myspace/', views.myspace),
    path('busqueda_residuos/', views.busqueda_residuos),
    path('buscar/', views.buscar),
]