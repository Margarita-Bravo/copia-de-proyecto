from django.db import models
from user.models import Cliente
from datetime import datetime

# Create your models here.


class Vehiculo(models.Model):
    modelo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='photos/%Y/%m/')
    tipo = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "vehiculo"
        verbose_name_plural = "vehiculos"
        verbose_name = "vehiculo"

    def get_thumbnail(self):
        if self.imagen:
            return self.imagen.url
        return ''

    def __str__(self):
        return self.modelo
