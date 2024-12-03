from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "categoria"
        verbose_name_plural = "categorias"
        verbose_name = "categoria"

    def __str__(self):
        return self.nombre
