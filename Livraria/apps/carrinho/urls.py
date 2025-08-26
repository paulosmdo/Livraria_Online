from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrinho, name="carrinho"),
    path('add_carrinho/', views.add_carrinho, name="add_item"),
    path('del_carrinho/', views.del_carrinho, name="del_item"),
]