from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # post views
    #path('', views.post_list, name='post_list'), basada en funciones
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    #path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'),
    path('<int:post_id>/comment/',
        views.post_comment, name='post_comment'),
]

# https://localhost:8000/blog/ el usuario al digitar esta url cae en la condicion path('', ...) y mostrala la lista de los posts
# En cambio si digita https://localhost:8000/blog/7 cae en la condicion path('8', ...) y lo manda a la vista del detalle del post deseado

