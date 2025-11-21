from django import forms
from .models import Livros

class LivrosForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['img', 'nome', 'autor', 'data_lancamento', 'categoria', 'usuario']

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['usuario'].widget = forms.HiddenInput()