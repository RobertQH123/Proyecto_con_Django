from .models import Profesional
from django import forms

# Formularios para la clase Profesional

class ProfesionalForm(forms.Form):
  nombre = forms.CharField(
          widget = forms.TextInput(attrs = {'placeholder' : 'Ingresa tu nombre'})
          )
  apellido = forms.CharField(
          widget = forms.TextInput(attrs = {'placeholder' : 'Ingresa tu apellido'})
          )
  fechaNac = forms.DateField(
          widget = forms.TextInput(attrs = 
              {'placeholder' : 'Ingresa tu fecha de nacimiento'}
              )
          )
  telefono = forms.IntegerField(
          widget = forms.TextInput(attrs =
              {'placeholder' : 'Ingresa tu numero de telefono'}
              )
          )
  profesion = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder' : 'Ingresa tu profesion'})
          )
  foto = forms.ImageField()
  class Meta:
    model = Profesional
    fields = [
        'nombre',
        'apellido',
        'fechaNac',
        'telefono',
        'profesion',
        'foto',
        ]
  def clean_nombre(self, *args, **kwargs):
    name = self.cleaned_data.get('nombre')
    if name.istitle():
      return name
    else:
      raise forms.ValidationError('La primera letra en mayusucula')
  def clean_apellido(self, *args, **kwargs):
    lastName = self.cleaned_data.get('apellido')
    if lastName.istitle():
      return lastName
    else:
      raise forms.ValidationError('La primera letra en mayusucula')
  def clean_telefono(self, *args, **kwargs):
    phone = self.cleaned_data.get('telefono')
    if phone.isnumeric():
      return phone
    else:
      raise forms.ValidationError('Ingrese un numero')
  def clean_profesion(self, *args, **kwargs):
    profession = self.cleaned_data.get('profesion')
    if profession.istitle():
      return profession
    else:
      raise forms.ValidationError('La primera letra en mayusucula')

