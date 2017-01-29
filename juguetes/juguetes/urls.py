from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^usuarios/', include('usuarios.urls')),
    url(r'^', include('website.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
