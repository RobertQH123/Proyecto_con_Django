from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
    )
from .models import Profesional
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from .forms import ProfesionalForm

# Create your views here.

class ProfesionalListView(ListView):
  model = Profesional

class ProfesionalDetailView(DetailView):
  model = Profesional

class ProfesionalCreateView(CreateView):
  model = Profesional
  fields = [
          'nombre',
          'apellido',
          'fechaNac',
          'telefono',
          'profesion',
          'foto',
          ] 

def ProfesionalAnotherCreate(request):
  form = ProfesionalForm()
  context = {
        'form' : form,
        }
  return render(request, 'profesionales/anotherCreate.html', context)

class ProfesionalUpdateView(UpdateView):
  model = Profesional
  fields = [
          'nombre',
          'apellido',
          'fechaNac',
          'telefono',
          'profesion',
          'foto',
          ] 

class ProfesionalDeleteView(DeleteView):
  model = Profesional
  success_url = reverse_lazy('profesionales:profesional-list')

class ProfesionalQueryView(View):
  def get(self, request, *args, **kwargs):
    return JsonResponse(list(Profesional.objects.values()), safe = False)

def servidorAngular(request, *args, **kwargs):
  return render(request, "http://localhost:4200/index.html", {})
