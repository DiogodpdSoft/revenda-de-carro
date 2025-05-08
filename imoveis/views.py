from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Imovel

def home(request):
    imoveis_destaque = Imovel.objects.filter(destaque=True)[:6]
    return render(request, 'imoveis/home.html', {
        'imoveis_destaque': imoveis_destaque
    })

def lista_imoveis(request):
    imoveis_lista = Imovel.objects.all()
    
    # Filtros
    cidade = request.GET.get('cidade')
    bairro = request.GET.get('bairro')
    tipo = request.GET.get('tipo')
    finalidade = request.GET.get('finalidade')
    preco_min = request.GET.get('preco_min')
    preco_max = request.GET.get('preco_max')
    quartos = request.GET.get('quartos')
    ano_min = request.GET.get('ano_min')
    ano_max = request.GET.get('ano_max')

    if cidade:
        imoveis_lista = imoveis_lista.filter(cidade__icontains=cidade)
    if bairro:
        imoveis_lista = imoveis_lista.filter(bairro__icontains=bairro)
    if tipo:
        imoveis_lista = imoveis_lista.filter(tipo=tipo)
    if finalidade:
        imoveis_lista = imoveis_lista.filter(finalidade=finalidade)
    if preco_min:
        imoveis_lista = imoveis_lista.filter(preco__gte=preco_min)
    if preco_max:
        imoveis_lista = imoveis_lista.filter(preco__lte=preco_max)
    if quartos:
        imoveis_lista = imoveis_lista.filter(quartos__gte=quartos)
    if ano_min:
        imoveis_lista = imoveis_lista.filter(ano_fabricacao__gte=ano_min)
    if ano_max:
        imoveis_lista = imoveis_lista.filter(ano_fabricacao__lte=ano_max)

    # Paginação
    paginator = Paginator(imoveis_lista, 9)  # 9 imóveis por página
    page = request.GET.get('page')
    imoveis = paginator.get_page(page)

    # Dados para os filtros
    cidades = Imovel.objects.values_list('cidade', flat=True).distinct()
    bairros = Imovel.objects.values_list('bairro', flat=True).distinct()
    tipos = dict(Imovel.TIPO_CHOICES)
    finalidades = dict(Imovel.FINALIDADE_CHOICES)

    context = {
        'imoveis': imoveis,
        'cidades': cidades,
        'bairros': bairros,
        'tipos': tipos,
        'finalidades': finalidades,
        # Manter filtros selecionados
        'filtros': {
            'cidade': cidade,
            'bairro': bairro,
            'tipo': tipo,
            'finalidade': finalidade,
            'preco_min': preco_min,
            'preco_max': preco_max,
            'quartos': quartos,
            'ano_min': ano_min,
            'ano_max': ano_max,
        }
    }
    
    return render(request, 'imoveis/lista_imoveis.html', context)

def detalhe_imovel(request, slug):
    imovel = get_object_or_404(Imovel, slug=slug)
    return render(request, 'imoveis/detalhe_imovel.html', {
        'imovel': imovel
    })
