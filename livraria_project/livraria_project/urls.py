"""
URL configuration for livraria_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from livraria.views import home
from livraria.views import adicionar_livro, lista_livros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('livraria.urls')),
    path('', home, name='home'),
    path('livros/adicionar/', adicionar_livro, name='adicionar_livro'),
    path('livros/', lista_livros, name='lista_livros'),
]
