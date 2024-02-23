from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request): # Lista completa de los posts
    posts = Post.published.all() # Nos conectamos con la BD, utilizamos el manager que definimos (published)
    return render(request,  # Rederizamos la respuesta y le pasamos los argumentos (todos los posts.)
                    'blog/post/list.html',
                    {'posts':posts})


def post_detail(request, id): # Detalle de un post el cual necesita un id para consultar un post en especifico y devolver el detalle.
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request,  
                    'blog/post/detail.html',
                    {'post':post})