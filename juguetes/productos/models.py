from django.db import models
from django.db.models import Sum


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    sku = models.CharField(max_length=5)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ManyToManyField(Categoria)
    # imagenes

    def stock(self):
        resultado_agregacion = self.stock_set.aggregate(Sum('cantidad'))
        return resultado_agregacion['cantidad__sum']

    def __str__(self):
        return self.nombre
