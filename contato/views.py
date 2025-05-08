from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MensagemContato
from django.urls import reverse

def contato(request):
    return render(request, 'contato/contato.html')

def enviar_mensagem(request):
    if request.method == 'POST':
        try:
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')
            mensagem = request.POST.get('mensagem')
            
            if not all([nome, email, telefone, mensagem]):
                messages.error(request, 'Por favor, preencha todos os campos.')
                return redirect('contato:contato')
            
            # Criar nova mensagem
            MensagemContato.objects.create(
                nome=nome,
                email=email,
                telefone=telefone,
                mensagem=mensagem
            )
            
            messages.success(request, 'Mensagem enviada com sucesso! Em breve entraremos em contato.')
            return redirect('contato:contato')
            
        except Exception as e:
            messages.error(request, 'Ocorreu um erro ao enviar sua mensagem. Por favor, tente novamente.')
            return redirect('contato:contato')
    
    return redirect('contato:contato')
