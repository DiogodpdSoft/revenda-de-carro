from django.urls import path
from . import views

app_name = 'contato'

urlpatterns = [
    path('', views.contato, name='contato'),
    path('enviar/', views.enviar_mensagem, name='enviar_mensagem'),
]
