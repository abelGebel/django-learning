from os import name
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    #products = Product.objects.all()
    products = Product.objects.filter(stock__gt=0)
    paginator = Paginator(products, 3)
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
