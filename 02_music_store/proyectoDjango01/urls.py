"""proyectoDjango01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from productos import views as productos_views
from django.conf import settings
from django.conf.urls.static import static
from productos.views import(DiscoListView,DiscoCreate, DiscoDelete,DiscoUpdate)


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('contacto/',views.contacto, name='contacto'),
    path('sign_up/',views.sign_up, name='sign_up'),
    path('tienda/',DiscoListView.as_view(),name='tienda'),
    path('create/',DiscoCreate.as_view(),name='create'),
    path('update/<int:pk>/', DiscoUpdate.as_view(), name='update'),		
    path('delete/<int:pk>/', DiscoDelete.as_view(), name='delete'),


]

# Configuracion extendida para mostrar las imagenes en modo debug
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)