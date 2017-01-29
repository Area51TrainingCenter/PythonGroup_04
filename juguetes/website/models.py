from django.db import models


class Contacto(models.Model):
    nombres = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=9, blank=True, null=True)
    mensaje = models.TextField()
