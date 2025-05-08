from django.urls import path
from . import views

app_name = 'imoveis'

urlpatterns = [
    path('', views.home, name='home'),
    path('imoveis/', views.lista_imoveis, name='lista_imoveis'),
    path('imovel/<slug:slug>/', views.detalhe_imovel, name='detalhe_imovel'),
]
