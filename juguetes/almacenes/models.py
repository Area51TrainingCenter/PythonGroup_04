from django.db import models

from productos.models import Producto


class Almacen(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Stock(models.Model):
    producto = models.ForeignKey(Producto)
    almacen = models.ForeignKey(Almacen)
    cantidad = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.producto.nombre

