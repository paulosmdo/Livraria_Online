from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from .models import Usuario
# from weasyprint import HTML
import tempfile
from apps.pedido.models import Pedido, Itens_Pedidos

def cadastro(req):
    if req.method == "GET":
        return render(req, "cadastro.html")
    else:
        nome = req.POST.get("nome", "")
        email = req.POST.get("email", "")    
        senha = req.POST.get("senha", "")
        endereco = req.POST.get("endereco")

        usuario = Usuario.objects.filter(email=email).first()
        if usuario:
            messages.error(req, "Já existe um conta com esse email")
            return redirect('cadastro')

        usuario = Usuario.objects.create_user(username=email, nome=nome, email=email, password=senha, endereco=endereco)
        usuario.save()

        return redirect('fazer_login')

def fazer_login(req):
    if req.method == "GET":
        return render(req, "login.html")
    else:
        email = req.POST.get("email", "")    
        senha = req.POST.get("senha", "")

        usuario = authenticate(username=email, password=senha)
        if usuario:
            login(req, usuario)
            messages.success(req, "Login realizado com sucesso!")
            return redirect('minha_conta')
        else:
            messages.error(req, "Email ou senha incorretos!")
            return redirect('fazer_login')

def sair(req):
    logout(req)
    messages.success(req, "Você foi deslogado")
    return redirect('catalogo')



@login_required(login_url="/conta/login/")
def minha_conta(req):
    pedidos = Pedido.objects.filter(id_usuario=req.user.id)
    return render(req, "minha_conta.html", {'pedidos': pedidos})


def exportar_pdf(req):
    if req.method == 'POST':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="pedidos.pdf"'

        id_pedido = req.POST.get('id_pedido')  
        if id_pedido:
            pedido = Pedido.objects.filter(id=id_pedido, id_usuario=req.user.id)
            itens_pedido = Itens_Pedidos.objects.filter(id_pedido=id_pedido)

            # html_string = render_to_string('pdf.html', {'pedidos': pedido, 'itens_pedidos': itens_pedido})
            
            # with tempfile.NamedTemporaryFile(delete=True) as output:
            #     HTML(string=html_string).write_pdf(output.name)
            #     output.seek(0)
            #     response.write(output.read())

            # return response
            return JsonResponse({'status': 'error', 'message': 'Metodo não existe'}, status=404)
        else:
            pedidos = Pedido.objects.filter(id_usuario=req.user.id)
            itens_pedidos = Itens_Pedidos.objects.filter(id_pedido__in=pedidos)

            # html_string = render_to_string('pdf.html', {'pedidos': pedidos, 'itens_pedidos': itens_pedidos})
            
            # with tempfile.NamedTemporaryFile(delete=True) as output:
            #     HTML(string=html_string).write_pdf(output.name)
            #     output.seek(0)
            #     response.write(output.read())

            # return response
            return JsonResponse({'status': 'error', 'message': 'Metodo não existe'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Metodo não existe'}, status=404)


