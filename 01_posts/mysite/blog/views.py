from django.shortcuts import render
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail

from django.views.decorators.http import require_POST

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
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED) # Busca el post resivido como parametro para buscarlo en la BD
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid(): # Debe tener un email correcto, un nombre que no se exeda de caracters, etc
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url()) # con build_absolute_uri nos aseguramos que el usuario al que le enviamos el email reciba la url de la forma https://misitio.com/blog/1
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'abelgebel@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})



def post_detail(request, year, month, day, post): # Detalle de un post el cual necesita un id para consultar un post en especifico y devolver el detalle.
    post = get_object_or_404(Post,  
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request,  
                    'blog/post/detail.html',
                    {'post':post,
                     'comments': comments,
                     'form': form})


@require_POST # Agregar funcionalidades si cambiar la funcion 
def post_comment(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED) # Busca el post resivido como parametro para buscarlo en la BD
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid(): # Debe tener un email correcto, un nombre que no se exeda de caracters, etc
        # Create Comment object but don't save to database yet
        comment = form.save(commit=False)
        # Assign the current post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(request, 'blog/post/comment.html', {'post': post,
                                                    'form': form,
                                                    'comment': comment})