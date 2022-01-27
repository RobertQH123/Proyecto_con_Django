from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
    )
from .models import Cliente
from django.urls import reverse_lazy
from django.http import JsonResponse
from .forms import ClienteForm

# Create your views here.

class ClienteListView(ListView):
  model = Cliente


class ClienteDetailView(DetailView):
  model = Cliente


class ClienteCreateView(CreateView):
  model = Cliente
  fields = [
        'nombre',
        'apellido',
        'telefono',
        'direccion',
        'fecha',
    ]

def ClienteAnotherCreate(request):
  form = ClienteForm()
  context = {
        'form' : form,
        }
  return render(request, 'clientes/anotherCreate.html', context)

class ClienteUpdateView(UpdateView):
  model = Cliente
  fields = [
        'nombre',
        'apellido',
        'telefono',
        'direccion',
        'fecha',
    ]

class ClienteDeleteView(DeleteView):
  model = Cliente 
  success_url = reverse_lazy('clientes:cliente-list')

class ClienteQueryView(View):
  def get(self, request, *args, **kwargs):
    return JsonResponse(list(Cliente.objects.values()), safe = False)
