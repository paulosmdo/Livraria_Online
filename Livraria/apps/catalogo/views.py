from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from apps.catalogo.models import Livro
import requests

URL_BASE="https://www.googleapis.com/books/v1/volumes"

def home(req):

    titulo = req.GET.get('titulo', '')
    autor = req.GET.get('autor', '')
    categoria = req.GET.get('categoria', '')
    pagina =  req.GET.get('pagina', 1)

    try:
        pagina = int(pagina)
    except ValueError:
        pagina = 1

    pagina_obj = {
        'anterior': 0 if pagina <= 0 else pagina - 1,
        'atual': 1 if pagina <= 0 else pagina,
        'proxima': 2 if pagina <= 0 else pagina + 1,
        'tem_proxima': True,
        'tem_anterior':False if pagina <= 1 else True,
    }
    

    if not titulo and not autor and not categoria: 
        init = 'programacaopython' 
    else: init = ''

    params= {
        'q': init +
        (f'intitle:{titulo}' if titulo else '')+
        (f' inauthor:{autor}' if autor else '')+
        (f' subject:{categoria}' if categoria else ''),
        'maxResults':12,
        'startIndex': pagina_obj['atual'],
        'orderBy': 'relevance'
    }

    print(params)

    response = requests.get(URL_BASE, params=params)

    livros = []

    if response.status_code == 200:
        data = response.json()
        livros = data.get('items', [])
        req.session['livros'] = livros
        

    return render(req, 'catalogo.html', {'livros': livros, 'titulo': titulo, 'autor': autor, 'categoria': categoria, 'pag_obj': pagina_obj})

def detalhes(req, livro_id):

    response = requests.get(f"{URL_BASE}/{livro_id}")

    if response.status_code == 200:
        data = response.json()
        livro = data.get('volumeInfo', None)
        preco = data.get('saleInfo', None)
        req.session['livros'] = [data]

    return render(req, 'detalhes.html', {'livro_id':livro_id, 'livro': livro, 'preco': preco})

def add_carrinho(req):
    if req.method == 'POST':
        try:
            livro_id = req.POST.get('item_id')        

            livros = req.session.get('livros', [])
            
            livro = next((l for l in livros if l['id'] == livro_id), None)            

            if not livro:
                return JsonResponse({'status': 'error', 'message': 'Não foi possivel adicionar o item'}, status=405)

            livro_banco = Livro.objects.filter(id=livro_id).first()
            volume = livro.get('volumeInfo', {})
            if not livro_banco:                
                livro_banco = Livro.objects.create(
                        id = livro['id'],
                        titulo = volume.get('title', 'Sem título'),
                        autor = ", ".join(volume.get('authors', [])),
                        publicadora = volume.get('publisher', ''),
                        data_publicacao = volume.get('publishedDate', None),
                        numero_paginas = volume.get('pageCount', 0),
                        capa = volume.get('imageLinks', {}).get('thumbnail', ''),
                        sinopse = volume.get('description', ''),
                        categoria = ", ".join(volume.get('categories', [])),
                        valor = livro.get('saleInfo', {}).get('retailPrice', {}).get('amount', 0)
                    )
                                
            else:
                livro_banco.valor = livro.get('saleInfo', {}).get('retailPrice', {}).get('amount', 0)
                
            livro_banco.save()

            
            carrinho = req.session.get('carrinho', [])

            encontrado = False
            for i in carrinho:
                if i['id_livro'] == livro['id']:
                    i['quantidade'] += 1
                    i['preco'] = livro.get('saleInfo', {}).get('retailPrice', {}).get('amount', 0)
                    i['valor_total'] = i['quantidade'] * livro.get('saleInfo', {}).get('retailPrice', {}).get('amount', 0)
                    encontrado = True
                    break
            

            if not encontrado:
                carrinho.append(
                    {
                        'id_livro': livro['id'],
                        'titulo': volume.get('title', 'Sem título'),
                        'preco':livro.get('saleInfo', {}).get('retailPrice', {}).get('amount', 0),
                        'quantidade': 1,
                        'valor_total':livro.get('saleInfo', {}).get('retailPrice', {}).get('amount', 0)
                    }
                )

            req.session['carrinho'] = carrinho
            messages.success(req, "Item adicionado ao carrinho")
            return JsonResponse({'status': 'success', 'message': 'Item adicionado ao carrinho'})

        except:
            messages.error(req, "Não foi possivel adicionar o item")
            return JsonResponse({'status': 'error', 'message': 'Não foi possivel adicionar o item'}, status=405)

    messages.error(req, "Método não permitido")
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)



def ping(req):
    return HttpResponse("pong")

