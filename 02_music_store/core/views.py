from django.shortcuts import HttpResponse,render

# Create your views here.

def home(request):
    return render(request,"core/home.html")

def contacto(request):
    return render(request,"core/contacto.html")

def sign_up(request):
    return render(request,"core/sign_up.html")