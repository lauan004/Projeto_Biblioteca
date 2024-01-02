from django.shortcuts import render, redirect
from .models import Livro
from .models import Autor
from .forms import LivroForm


def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livraria/lista_livros.html', {'livros': livros})

def detalhes_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    return render(request, 'livraria/detalhes_livro.html', {'livro': livro})

def home(request):
    return render(request, 'livraria/home.html')

def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')  # Redireciona para a lista de livros após a inclusão
    else:
        form = LivroForm()

    return render(request, 'livraria/adicionar_livro.html', {'form': form})

