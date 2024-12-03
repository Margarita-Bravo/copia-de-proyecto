from django.contrib import admin
from .models import Sucursal
# Register your models here.


class SucursalAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'telefono', 'email')
    list_display_links = ('direccion', 'telefono', 'email')
    search_fields = ('direccion', 'telefono', 'email')
    list_per_page = 25


admin.site.register(Sucursal, SucursalAdmin)
