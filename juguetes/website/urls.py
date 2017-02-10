from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from website import views

urlpatterns = [
    url(r'^buscar/?$', views.Buscar.as_view(), name='busqueda'),
    url(r'^contacto/?$', views.ContactoView.as_view(), name='contacto'),
    url(r'^producto/(?P<pk>\d+)/?$', views.DetalleProducto.as_view(), name='detalle_producto'),
    url(r'^agregar-carrito/?$',
        csrf_exempt(views.AgregarCarrito.as_view()),
        name='agregar_carrito'),
    url(r'^carrito/?$', views.Carrito.as_view(), name='carrito'),
    url(r'^checkout/?$', views.Checkout.as_view(), name='checkout'),
    url(r'^gracias/?$', views.Gracias.as_view(), name='gracias'),
    url(r'^$', views.Home.as_view(), name='home')
]
