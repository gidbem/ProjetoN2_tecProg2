from django import forms
from .models import Jogo, Avaliacao


class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = '__all__'
        widgets = {
            'data_lancamento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'plataformas': forms.CheckboxSelectMultiple,
        }


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nome_visitante', 'nota', 'comentario']