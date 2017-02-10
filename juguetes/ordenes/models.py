from django.contrib.auth.models import User
from django.db import models

from productos.models import Producto


class Orden(models.Model):
    usuario = models.ForeignKey(User)
    productos = models.ManyToManyField(Producto)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    direccion = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=(
            ('recibido', 'Recibido'),
            ('despachado', 'Despachado')
        )
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super(Orden, self).__init__(*args, **kwargs)
        self.estado_anterior = self.estado

    def save(self, *args, **kwargs):
        if self.estado != self.estado_anterior and self.estado_anterior == 'recibido':
            for producto in self.productos.all():
                stock = producto.stock_set.filter(cantidad__gt=0).first()
                stock.cantidad -= 1
                stock.save()
        return super(Orden, self).save(*args, **kwargs)

    def __str__(self):
        return self.usuario.first_name
