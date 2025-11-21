from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('ver_livro/<int:id>', views.ver_livros, name = 'ver_livros'),
    path('pg_principal/', views.pg_principal, name = 'pg_principal'),
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),
    path('editar_livro/<int:id>', views.editar_livro, name='editar_livro'),
    path('excluir_livro/<int:id>', views.excluir_livro, name='excluir_livro'),
    path('devolver_livro/', views.devolver_livro, name='devolver_livro'),
    path('livros_emprestados/', views.livros_emprestados, name='livros_emprestados'),
    path('cadastrar_emprestimo/', views.cadastrar_emprestimo, name='cadastrar_emprestimo'),
]