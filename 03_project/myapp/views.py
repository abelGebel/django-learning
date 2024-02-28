from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Project, Task

# Create your views here.

def index(request):
    title = 'Django Curse'
    return render(request, "index.html", 
                  {'title': title})

def hello(request, username):
    return HttpResponse("<h2>hello %s</h2>" % username)

def about(request): 
    return render(request, "about.html")

def projects(request):
        projects = Project.objects.all()
        return render(request, "projects.html", {'projects': projects})


def Tasks(request):
    # task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, "tasks.html", {'tasks': tasks})
