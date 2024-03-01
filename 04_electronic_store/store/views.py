import django
from django.shortcuts import get_object_or_404, redirect, render
from mysite import settings
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
#from captcha.client import captcha
from django.core.exceptions import ValidationError

# Create your views here.

def home(request):
    productos_oferta = Product.objects.filter(in_offer=True)
    return render(request, 'home.html', {'productos_oferta': productos_oferta})



def contact(request):
    return render(request, 'contact.html')

def products(request):
    #products = Product.objects.all()
    products = Product.objects.filter(stock__gt=0)
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {'products': products})

def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def comprar_producto(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)
    if producto.stock > 0:
        producto.stock -= 1
        producto.save()
    return products(request)


def enviar_email(request):
    if request.method =="POST":
        name = request.POST["nombre"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["mensaje"]

        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': message
        })

        # Verifica el captcha
        #captcha_response = request.POST.get('g-recaptcha-response', '')
        #if not captcha.verify(settings.RECAPTCHA_SECRET_KEY, captcha_response, remote_ip=request.META['REMOTE_ADDR']):
        #    raise ValidationError('Captcha inválido')

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['abelgebel@gmail.com']
        )
        
        email.fail_silently = False
        email.send()

        messages.success(request, 'El correo se ha enviado correctamente. ')
        return redirect('contact')