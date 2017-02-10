from django.contrib import admin

from almacenes.models import Almacen, Stock


class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre',)


class StockAdmin(admin.ModelAdmin):
    list_display = ('producto', 'almacen', 'cantidad',)
    list_filter = ('almacen', 'producto',)
    search_fields = ('producto__nombre',)

admin.site.register(Almacen, AlmacenAdmin)
admin.site.register(Stock, StockAdmin)
