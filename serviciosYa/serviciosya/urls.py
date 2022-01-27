"""serviciosya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import myHome
from django.conf import settings # IMPORTADO POR VS CODE
from django.conf.urls.static import static # IMPORTADO POR VS CODE

urlpatterns = [
    path('', myHome , name="Inicio"),
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('profesionales/', include('profesionales.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Esto enlaza cada path con nuestra carpeta media 
# https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development