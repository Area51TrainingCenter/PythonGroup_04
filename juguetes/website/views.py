from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import TemplateView

import requests

from ordenes.models import Orden
from productos.models import Producto
from website.forms import ContactoForm, CheckoutForm


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super(Home, self).get_context_data(**kwargs)
        contexto['productos'] = Producto.objects.in_stock().order_by('-id')[:5]
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


class AgregarCarrito(View):
    def post(self, request):
        pk = request.POST['id']
        if 'carrito' not in request.session:
            request.session['carrito'] = []

        if pk not in request.session['carrito']:
            request.session['carrito'] += [pk]
        return JsonResponse({'success': True})


class Carrito(ListView):
    template_name = 'carrito.html'
    model = Producto

    def get_queryset(self):
        queryset = super(Carrito, self).get_queryset()
        queryset = queryset.filter(id__in=self.request.session.get('carrito', []))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(Carrito, self).get_context_data(**kwargs)
        context['total'] = self.get_queryset().aggregate(Sum('precio'))['precio__sum']
        return context


class Checkout(FormView):
    template_name = 'checkout.html'
    form_class = CheckoutForm

    def get_context_data(self, **kwargs):
        contexto = super(Checkout, self).get_context_data(**kwargs)
        productos = Producto.objects.filter(id__in=self.request.session.get('carrito', []))
        contexto['total'] = productos.aggregate(Sum('precio'))['precio__sum']
        contexto['productos'] = productos
        return contexto

    def form_valid(self, form):
        direccion = form.cleaned_data['direccion']
        usuario = self.request.user
        contexto = self.get_context_data()
        total = contexto['total']
        productos = contexto['productos']
        estado = 'recibido'

        orden = Orden()
        orden.usuario = usuario
        orden.precio = total
        orden.direccion = direccion
        orden.estado = estado
        orden.save()

        for producto in productos:
            orden.productos.add(producto)

        del self.request.session['carrito']

        return redirect('gracias')


class Gracias(TemplateView):
    template_name = 'gracias.html'
