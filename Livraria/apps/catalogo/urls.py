from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='catalogo'),
    path('adicionar/', views.add_carrinho, name='add_carrinho'),
    path('<str:livro_id>/', views.detalhes, name='detalhes_livro'),
    

]