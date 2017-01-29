from django.contrib import admin

from website.models import Contacto


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'email', 'telefono')

admin.site.register(Contacto, ContactoAdmin)
