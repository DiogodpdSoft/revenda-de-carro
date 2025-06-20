from django.shortcuts import render, get_object_or_404
from .models import Carro

# Create your views here.

def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carros/lista_carros.html', {'carros': carros})

def detalhe_carro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    return render(request, 'carros/detalhe_carro.html', {'carro': carro})
