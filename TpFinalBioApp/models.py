from django.db import models

from TpFinalBio.settings.base import BASE_DIR


class FastaFile(models.Model):

    file = models.FileField(upload_to=  'secuences/files/')

class Secuence(models.Model):

    address = models.CharField(max_length=500)
    source = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    bio_id = models.TextField()
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)
    length = models.IntegerField()
    upload_id = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.content

