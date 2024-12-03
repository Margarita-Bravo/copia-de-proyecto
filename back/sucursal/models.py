from django.db import models
from django.core.validators import RegexValidator
from categoria.models import Categoria
from datetime import datetime

# Create your models here.


class Sucursal(models.Model):
    direccion = models.CharField(max_length=100)
    telefono_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="El número de teléfono debe estar en el formato: '+999999999'."
    )
    telefono = models.CharField(
        max_length=15,
        validators=[telefono_regex],
        unique=True
    )
    email = models.EmailField()

    class Meta:
        db_table = "sucursal"
        verbose_name_plural = "sucursales"
        verbose_name = "sucursal"

    def __str__(self):
        return self.direccion
