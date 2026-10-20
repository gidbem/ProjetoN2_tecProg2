from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Jogo
from .forms import JogoForm, AvaliacaoForm


def pagina_inicial(request):
    jogo_destaque = Jogo.objects.filter(destaque=True).first()
    jogos = Jogo.objects.all()
    if jogo_destaque:
        jogos = jogos.exclude(pk=jogo_destaque.pk)
    context = {'jogo_destaque': jogo_destaque, 'jogos': jogos}
    return render(request, 'catalogo/index.html', context)


def detalhes(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    avaliacoes = jogo.avaliacao_set.all()  # se usou related_name, troque aqui

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.jogo = jogo
            avaliacao.save()
            return redirect('detalhes', pk=jogo.pk)
    else:
        form = AvaliacaoForm()

    context = {'jogo': jogo, 'avaliacoes': avaliacoes, 'form': form}
    return render(request, 'catalogo/detalhes.html', context)


@login_required
def dashboard(request):
    jogos = Jogo.objects.all()
    return render(request, 'catalogo/dashboard.html', {'jogos': jogos})


@login_required
def jogo_criar(request):
    form = JogoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'catalogo/jogo_form.html', {'form': form, 'titulo': 'Adicionar jogo'})


@login_required
def jogo_editar(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    form = JogoForm(request.POST or None, request.FILES or None, instance=jogo)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'catalogo/jogo_form.html', {'form': form, 'titulo': 'Editar jogo'})


@login_required
def jogo_excluir(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        jogo.delete()
        return redirect('dashboard')
    return render(request, 'catalogo/jogo_confirmar_exclusao.html', {'jogo': jogo})


