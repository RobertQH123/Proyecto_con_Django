from django import forms

# Formularios para la clase Cliente

class ClienteForm(forms.Form):
  nombre = forms.CharField(
          widget = forms.TextInput(attrs = {'placeholder' : 'Ingresa tu nombre'})
          )
  apellido = forms.CharField(
          widget = forms.TextInput(attrs = {'placeholder' : 'Ingresa tu apellido'})
          )
  telefono = forms.IntegerField(
          widget = forms.TextInput(attrs = 
              {'placeholder' : 'Ingresa tu numero de celular'}
              )
          )
  direccion = forms.CharField(
          widget = forms.TextInput(attrs = {'placeholder' : 'Ingresa tu direccion'})
          )
  fecha = forms.DateField(
          widget = forms.TextInput(attrs = 
              {'placeholder' : 'Ingresa tu fecha de nacimiento'}
              )
          )

