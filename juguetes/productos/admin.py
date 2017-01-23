from django.contrib import admin

from productos.models import Producto, Categoria


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nombre', 'precio')
    search_fields = ('sku', 'nombre')


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)