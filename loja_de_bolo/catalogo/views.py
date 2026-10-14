from django.shortcuts import render, redirect, get_object_or_404
from .models import Jogo


def pagina_inicial(request):
    return render(request, 'catalogo/index.html')

def jogos(request):
    jogo_destaque = Jogo.objects.filter(destaque=True).first()
    if jogo_destaque:
        jogos = Jogo.objects.exclude(pk=jogo_destaque.pk)
    else:
        jogos = Jogo.objects.all()
    context = {
        'jogo_destaque': jogo_destaque,
        'jogos': jogos,
    }
    return render(request, 'jogos.html', context)


