from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/',views.contact, name="contact"),
    path('products/',views.products, name="products"),
    path('search/', views.search, name='search'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:producto_id>/comprar/', views.comprar_producto, name='comprar_producto'),

]

# Configuracion extendida para mostrar las imagenes en modo debug
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)