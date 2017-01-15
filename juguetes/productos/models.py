from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)


class Producto(models.Model):
    sku = models.CharField(max_length=5)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ManyToManyField(Categoria)
    # imagenes

    def __str__(self):
        return self.nombre
