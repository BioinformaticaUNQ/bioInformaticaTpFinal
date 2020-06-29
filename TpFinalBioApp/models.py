from django.db import models


class Geolocalizador(models.Model):
    
    latitud = models.CharField(max_length=250)
    longitud = models.CharField(max_length=250)


class Secuencia(models.Model):

    adress = models.CharField(max_length=500)
    latitud = models.CharField(max_length=20)
    length = models.IntegerField()
    content = models.TextField()
    file = models.FileField(upload_to= 'secuences/files/')

    def __str__(self):
        return self.content

