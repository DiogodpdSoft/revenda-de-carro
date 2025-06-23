from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.lista_carros, name='lista_carros'),
    path('<int:carro_id>/', views.detalhe_carro, name='detalhe_carro'),
] 