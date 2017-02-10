from django.contrib import admin

from ordenes.models import Orden


class OrdenAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'precio', 'direccion', 'estado')
    list_filter = ('estado',)
    search_fields = ('usuario',)

admin.site.register(Orden, OrdenAdmin)
