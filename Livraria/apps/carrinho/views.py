from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse, JsonResponse

def carrinho(req):
    itens_do_carrinho = req.session.get('carrinho', [])
    print(itens_do_carrinho)
    return render(req, 'carrinho.html', {'carrinho':itens_do_carrinho})

def add_carrinho(req):
    if req.method == 'POST':
        try:
            item_id = req.POST.get('item_id')  
            
            itens_do_carrinho = req.session.get('carrinho', [])
            
            for i in itens_do_carrinho:
                if i['id_livro'] == item_id:
                    i['quantidade'] += 1
                    i['valor_total'] = i['quantidade'] * i['preco'] 
                    break

            req.session['carrinho'] = itens_do_carrinho

            return JsonResponse({'status': 'success', 'message': 'Item adicionado ao carrinho'})
        except:
           return JsonResponse({'status': 'error', 'message': 'Não foi possivel adicionar o item'}, status=405)
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)

def del_carrinho(req):
    if req.method == 'POST':
        try:
            item_id = req.POST.get('item_id')  
            
            itens_do_carrinho = req.session.get('carrinho', [])
            
            for i, item in enumerate(itens_do_carrinho):
                if item['id_livro'] == item_id:
                    item['quantidade'] -= 1
                    item['valor_total'] = item['quantidade'] * item['preco'] 

                    if item['quantidade'] <= 0:
                        itens_do_carrinho.pop(i)
                        
                    break

            req.session['carrinho'] = itens_do_carrinho

            return JsonResponse({'status': 'success', 'message': 'Item removido do carrinho'})
        except:
           return JsonResponse({'status': 'error', 'message': 'Não foi possivel remover o item'}, status=405)
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)