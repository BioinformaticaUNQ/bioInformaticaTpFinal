from django.db import models


class Geolocalizador(models.Model):
    
    latitud = models.CharField(max_length=250)
    longitud = models.CharField(max_length=250)


class FastaFile(models.Model):

    file = models.FileField(upload_to= 'secuences/files/')

class Secuence(models.Model):

    adress = models.CharField(max_length=500)
    bio_id = models.TextField()
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)
    length = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.content

