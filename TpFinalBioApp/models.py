from django.db import models


class Geolocalizador(models.Model):
    
    latitud = models.CharField(max_length=250)
    longitud = models.CharField(max_length=250) 