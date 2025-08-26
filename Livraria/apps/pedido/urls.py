from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.home, name="checkout"),
    path('finalizar/', views.finalizar_pedido, name="finalizar_pedido"),
    path('cancelar/', views.cancelar_pedido, name="cancelar_pedido")

]