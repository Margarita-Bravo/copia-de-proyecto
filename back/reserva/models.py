from django.db import models
from servicio.models import Servicio
from sucursal.models import Sucursal
from user.models import Cliente

# Create your models here.


class Reserva(models.Model):
    fecha = models.DateTimeField()
    hora = models.TimeField()
    ESTADOS_RESERVA = (
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    )
    estado_reserva = models.CharField(max_length=20, choices=ESTADOS_RESERVA)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = "reserva"
        verbose_name_plural = "reservas"
        verbose_name = "reserva"

    def __str__(self):
        return self.estado_reserva
