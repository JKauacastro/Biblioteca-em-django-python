from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimos
from .forms import LivrosForm
from django import forms

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        form = LivrosForm()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].qyueryset = Usuario.objects.all()
        usuarios = Usuario.objects.all()
        return render(request, 'home.html', {'livros': livros, 'form': form, 'usuarios':usuarios})
    else:
        return redirect('/auth/login/?status=2')
    
def ver_livros(request, id):
    if request.session.get('usuario'):
            livros = Livros.objects.get(id = id)
            if request.session.get('usuario'):
                livros = Livros.objects.get(id = id)
                emprestimos = Emprestimos.objects.filter(livro = livros)
                form = LivrosForm()
                usuarios = Usuario.objects.all()
                form.fields['usuario'].initial = request.session['usuario']
                form.fields['categoria'].qyueryset = Usuario.objects.all()
                return render(request, 'ver_livro.html', {'livro': livros, 'form': form, 'emprestimos': emprestimos, 'livro_id': id, 'usuarios':usuarios})
            else:
                return redirect('/auth/cadastro/?status=5')
    return redirect('/auth/login/?status=2')

def pg_principal(request):
    livros = Livros.objects.all().distinct().order_by('id')
    return render(request, 'pg_principal.html', {'livros': livros})

def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivrosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/livro/home/?status=6')
        else:
            return redirect('/livro/home/?status=7')

def editar_livro(request):
    livro_id = request.POST.get('livro_id')
    nome_livro = request.POST.get('nome_livro')
    autor = request.POST.get('autor')
    co_autor = request.POST.get('co_autor')
    categoria_id = request.POST.get('categoria_id')

    categoria = Categoria.objects.get(id = categoria_id)
    livro = Livros.objects.get(id = livro_id)
    if livro.usuario.id == request.session['usuario']:
        livro.nome = nome_livro
        livro.autor = autor
        livro.co_autor = co_autor
        livro.categoria = categoria
        livro.save()
        return redirect(f'/livro/ver_livro/{livro_id}')
    else:
        return redirect('/auth/sair')
    
def excluir_livro(request, id):
    livro = Livros.objects.get(id = id).delete()
    return redirect('/livro/home')

def devolver_livro(request):
    #livro_devolver = Livros.objects.get(id = id)
    #livro_devolver.emprestado = False
    #livro_devolver.save()
    return HttpResponse('temporario')

def livros_emprestados(request):
    livros = Livros.objects.all().distinct().order_by('id')
    return render(request, 'livros_emprestados.html', {'livros': livros})

def cadastrar_emprestimo(request):
    return HttpResponse('test')