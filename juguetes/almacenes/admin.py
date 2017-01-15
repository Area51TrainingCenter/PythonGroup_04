from django.contrib import admin

from almacenes.models import Almacen, Stock

admin.site.register(Almacen)
admin.site.register(Stock)