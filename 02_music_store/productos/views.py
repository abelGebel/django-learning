from django.shortcuts import render

from .models import Disco
from django.urls import reverse, reverse_lazy

from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from productos.forms import DiscoForm

# Create your views here.
class DiscoListView(ListView):
    model= Disco

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class DiscoCreate(CreateView):
    model=Disco
    form_class = DiscoForm
    success_url = reverse_lazy('tienda')


class DiscoUpdate(UpdateView):
    model = Disco
    #fields = ['nombre', 'descripcion', 'imagen']
    form_class = DiscoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('tienda')+'?Actualizado'

class DiscoDelete(DeleteView):
    model = Disco
    def get_success_url(self):
        return reverse_lazy('tienda')+'?Eliminado'   

# def tienda(request):
#     discos = Disco.objects.all()
#     return render(request, "productos/tienda.html", {'misDiscos':discos})