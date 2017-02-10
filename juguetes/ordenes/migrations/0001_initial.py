# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 18:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0002_auto_20170114_1448'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('direccion', models.TextField()),
                ('estado', models.CharField(choices=[('recibido', 'Recibido'), ('despachado', 'Despachado')], max_length=20)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('productos', models.ManyToManyField(to='productos.Producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
