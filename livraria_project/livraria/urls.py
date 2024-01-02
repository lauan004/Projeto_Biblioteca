from django.urls import path
from .views import home, lista_livros, detalhes_livro
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('lista_livros', lista_livros, name='lista_livros'),
    path('livro/<int:livro_id>/', detalhes_livro, name='detalhes_livro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)