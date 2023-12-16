from django.shortcuts import render
from .models import Livro
from .models import Autor


def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livraria/lista_livros.html', {'livros': livros})

def detalhes_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    return render(request, 'livraria/detalhes_livro.html', {'livro': livro})

def home(request):
    return render(request, 'livraria/home.html')
# Create your views here.
