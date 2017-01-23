from django.db import models

from productos.models import Producto


class Almacen(models.Model):
    nombre = models.CharField(
        verbose_name='Nombre de almacén',
        max_length=50
    )

    direccion = models.TextField(
        verbose_name='Dirección',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Almacén'
        verbose_name_plural = 'Almacenes'


class Stock(models.Model):
    producto = models.ForeignKey(Producto)
    almacen = models.ForeignKey(Almacen)
    cantidad = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.producto.nombre

