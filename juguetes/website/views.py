from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import TemplateView

import requests

from productos.models import Producto
from website.forms import ContactoForm
from website.models import Contacto


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super(Home, self).get_context_data(**kwargs)
        contexto['nombre'] = 'Moisés'
        contexto['productos'] = Producto.objects.all().order_by('-id')[:5]
        return contexto


class Buscar(ListView):
    template_name = 'busqueda.html'
    model = Producto

    def get_queryset(self):
        queryset = super(Buscar, self).get_queryset()
        termino = self.request.GET.get('q', '')
        queryset = queryset.filter(nombre__icontains=termino)
        return queryset


class ContactoView(FormView):
    template_name = 'contacto.html'
    form_class = ContactoForm

    def form_valid(self, form):
        form.save()
        nombres = form.cleaned_data['nombres']
        email = form.cleaned_data['email']
        telefono = form.cleaned_data['telefono']
        mensaje = form.cleaned_data['mensaje']
        requests.post(
            'https://api.mailgun.net/v3/sandboxed7d5bcac9fd4247bb8e22e8a469eecb.mailgun.org/messages',
            auth=('api', 'key-4fab09ec3e1a3a248aaeb5ea0b02e24b'),
            data={'from': 'Moisés <moi@ses.mailgun.org>',
                  'to': ['xpktro@gmail.com'],
                  'subject': 'Formulario de contacto',
                  'text': '{} ({} - {}) te ha enviado el siguiente mensaje: {}'.format(nombres, email, telefono, mensaje)})
        return redirect('home')


class DetalleProducto(DetailView):
    template_name = 'detalle.html'
    model = Producto
