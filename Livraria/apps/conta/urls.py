from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.fazer_login, name="fazer_login"),
    path('minha/', views.minha_conta, name="minha_conta"),
    path('sair/', views.sair, name="sair_da_conta"),
    path('exportar/pdf/', views.exportar_pdf, name='exportar_pdf'),
]