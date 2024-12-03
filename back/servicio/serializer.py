from rest_framework import serializers
from .models import Servicio

class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Servicio
        fields=['id','nombre','imagen','descripcion','precio','fecha_creacion']
