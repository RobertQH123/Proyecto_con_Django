from django.urls import path
from .views import (
    ProfesionalListView,
    ProfesionalDetailView,
    ProfesionalCreateView,
    ProfesionalUpdateView,
    ProfesionalDeleteView,
    ProfesionalQueryView,
    )
from profesionales.views import *

app_name = 'profesionales'
urlpatterns = [
    path('', ProfesionalListView.as_view(), name = 'profesional-list'),
    path('<int:pk>/', ProfesionalDetailView.as_view(), name = 'profesional-detail'),
    path('create/', ProfesionalCreateView.as_view(), name = 'profesional-create'),
    path('<int:pk>/update/', ProfesionalUpdateView.as_view(), name = 'profesional-update'),
    path('<int:pk>/delete/', ProfesionalDeleteView.as_view(), name = 'profesional-delete'),
    path('query/', ProfesionalQueryView.as_view(), name = 'profesional-query'),
    path('anotherCreate/', ProfesionalAnotherCreate, name = 'profesional-anotherCreate'),
    path('inicioAngular/', servidorAngular, name = 'servidor-angular'),
    ]
