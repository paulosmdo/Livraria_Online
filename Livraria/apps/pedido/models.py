from django.db import models
from apps.conta.models import Usuario
from apps.catalogo.models import Livro

class Pedido(models.Model):
    ENUM_STATUS = [(1,'Pendente'), (2,'Pago'), (3,'Cancelado')]
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedido_usuario')
    status = models.IntegerField(choices=ENUM_STATUS, default=1)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)

class Itens_Pedidos(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_pedidos')
    id_livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    titulo_livro = models.CharField(max_length=300, blank=True, null=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)