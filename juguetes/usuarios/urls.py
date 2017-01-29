from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from usuarios import views

urlpatterns = [
    url(r'^registro/?$', views.Registro.as_view(), name='registro'),
    url(r'^login/?$', views.Login.as_view(), name='login'),
    url(r'^logout/?$', views.Logout.as_view(), name='logout'),
    url(r'^perfil/?$',
        login_required(views.Perfil.as_view(), login_url=reverse_lazy('login')),
        name='perfil'),
]
