from turtle import title
from django.db import models

myapp_tipo = [
    (1, 'Emisor'),
    (2, 'Remitente')
]
myapp_ubicacion = [
    (1, 'Arica y Parinacota'),
    (2, 'Tarapacá'),
    (3, 'Antofagasta'),
    (4, 'Atacama'),
    (5, 'Coquimbo'),
    (6, 'Valparaíso'),
    (7, 'Metropolitana'),
    (8, 'Libertador General Bernardo OHiggins'),
    (9, 'Maule'),
    (10, 'Ñuble'),
    (11, 'Biobío'),
    (12, 'Araucanía'),
    (13, 'Los Ríos'),
    (14, 'Los Lagos'),
    (15, 'Aysén'),
    (16, 'Magallanes')
]
myapp_residuos = [
    (1, 'Plástico'),
    (2, 'Latas'),
    (3, 'Residuos Orgánicos'),
    (4, 'Residuos Metalicos'),
    (5, 'Ropa/Tela'),
    (6, 'Cartón'),
    (7, 'Vidrios'),
    (8, 'Madera'),
    (9, 'Papel'),
    (10, 'Baterías y pilas'),
    (11, 'Chatarra'),
    (12, 'Otros'),
]


# Create your models here.
class info(models.Model):
    nombre = models.CharField(max_length=30)
    empresa = models.CharField(max_length=20)
    
class select(models.Model):
    tipo = models.IntegerField(
        null=False, blank=False,
        choices= myapp_tipo
    )
    ubicacion = models.IntegerField(
        null=False, blank=False,
        choices= myapp_ubicacion
    )
    residuos = models.IntegerField(
        null=False, blank=False,
        choices= myapp_residuos
    )

