from django.db import models
from datetime import date
from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length = 30)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome

#class Emprestimos(models.Model):


class Livros(models.Model):
    img = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank = True)
    data_lancamento = models.DateField(blank = True, null = True)
    emprestado = models.BooleanField(default = False)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateTimeField(blank = True, null = True)
    data_devolucao = models.DateTimeField(blank = True, null = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)
    

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome