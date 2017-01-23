from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from productos.models import Producto


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


class DetalleProducto(DetailView):
    template_name = 'detalle.html'
    model = Producto
