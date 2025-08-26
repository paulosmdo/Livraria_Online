from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Pedido, Itens_Pedidos
from apps.catalogo.models import Livro

def home(req):
    itens_do_carrinho = req.session.get('carrinho', [])
    if not itens_do_carrinho:
        messages.error(req, "Carrinho Vazio! Vá em \"Minha conta\" para verificar os pedidos pendentes")
        return redirect('catalogo')

    valor_total = 0
    if req.user.is_authenticated:        

        if itens_do_carrinho:            
            for item in itens_do_carrinho:
                valor_total += item['valor_total']

            #usuario = Usuario.objects.filter(id=req.user.id).first()

            pedido = Pedido.objects.create(id_usuario = req.user, status=1, valor_total=valor_total)
            for item in itens_do_carrinho:
                livro = Livro.objects.filter(id=item['id_livro']).first()
                Itens_Pedidos.objects.create(id_pedido = pedido, id_livro = livro, titulo_livro = livro.titulo, preco= item['preco'], quantidade = item['quantidade'], valor_total=item['valor_total'])
            
            req.session['carrinho'] = []


        return render(req, 'checkout.html', {'id_pedido':pedido.id, 'carrinho':itens_do_carrinho, 'valor_total':valor_total})
    return render(req, 'checkout.html')

def finalizar_pedido(req):
    if req.method == 'POST':
        try:
            id_pedido = req.POST.get('id_pedido')  
            
            pedido = Pedido.objects.filter(id=id_pedido).first();

            if pedido:
                pedido.status = 2
                pedido.save()  
                messages.success(req, "Pedido pago com sucesso!") 
                return JsonResponse({'status': 'success', 'message': 'Pedido pago com sucesso!'})
            else:
                print("entrou1")
                messages.error(req, "Falha ao pagar o pedido, verificar pedidos pendentes em Minha Conta")
                return JsonResponse({'status': 'error', 'message': 'Falha ao pagar o pedido, verificar pedidos pendentes em Minha Conta'}, status=405)  
        except:
            print("entrou2")
            messages.error(req, "Falha ao pagar o pedido, verificar pedidos pendentes em Minha Conta")
    return JsonResponse({'status': 'error', 'message': 'Falha ao pagar o pedido, verificar pedidos pendentes em Minha Conta'}, status=405)

def cancelar_pedido(req):
    if req.method == 'POST':
        try:
            id_pedido = req.POST.get('id_pedido')  
            
            pedido = Pedido.objects.filter(id=id_pedido).first();

            if pedido:
                pedido.status = 3
                pedido.save()  
                messages.success(req, "Pedido cancelado com sucesso!") 
                return JsonResponse({'status': 'success', 'message': 'Pedido cancelado com sucesso!'})
            else:
                messages.error(req, "Falha ao cancelado o pedido")
                return JsonResponse({'status': 'error', 'message': 'Falha ao cancelado o pedido'}, status=405)  
        except:
            messages.error(req, "Falha ao cancelado o pedido")
    return JsonResponse({'status': 'error', 'message': 'Falha ao cancelado o pedido'}, status=405)
