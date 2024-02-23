from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class PublishedManager(models.Manager): # Podemos crear un manager
    def get_queryset(self): # Sobreescribimos el metodo
        return super().get_queryset()\
                     .filter(status=Post.Status.PUBLISHED)
# Accedemos a todas las sentencias de nuestra clase padre pero aplicando un filtro

class Post(models.Model):
    class Status(models.TextChoices): # Crea una clase interna para seleccionar las opciones
        DRAFT = 'DF', 'Draft' # (Borrrador)
        PUBLISHED = 'PB', 'Published' # (Publicado)
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250) # Facilita busquedas.
    author = models.ForeignKey(User, # Tabla de autores, un autor tiene muchos posts... (esto ya viene incluido en django)
                               on_delete=models.CASCADE, # Si elimino el usuario Abel, todos sus posts se van a eliminar
                               related_name='blog_posts')
    body = models.TextField()

    # Campos relacionados con las fechas:
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    # Definimos nuestros manages dentro de nuestro modelo
    objects = models.Manager()
    published = PublishedManager()

    class Meta: # Clase interna (ordenamiento inverso de los posts)
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self): # Metodo que muestra el titulo del post en la adm de django
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.id])