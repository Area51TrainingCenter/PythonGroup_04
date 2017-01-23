from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^buscar/?$', views.Buscar.as_view(), name='busqueda'),
    url(r'^producto/(?P<pk>\d+)/?$', views.DetalleProducto.as_view(), name='detalle_producto'),
    url(r'^$', views.Home.as_view(), name='home')
]
