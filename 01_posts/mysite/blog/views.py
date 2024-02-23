from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm


# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_list(request):     # Lista completa de los posts
    post_list = Post.published.all()     # Nos conectamos con la BD, utilizamos el manager que definimos (published)
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        # if page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request,      # Rederizamos la respuesta y le pasamos los argumentos (todos los posts.)
                    'blog/post/list.html',
                    {'posts':posts})


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form})



def post_detail(request, year, month, day, post): # Detalle de un post el cual necesita un id para consultar un post en especifico y devolver el detalle.
    post = get_object_or_404(Post,  
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,  
                    'blog/post/detail.html',
                    {'post':post})