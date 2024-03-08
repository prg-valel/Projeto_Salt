from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Dados_usuario

def index(request):
    return HttpResponseRedirect('/plataform')

def plataform_page(request):
    return render(request, 'plataform.html')

def login_user_page(request):
    return render(request, 'login_user.html')

'''
def login_admin_page(request):
    return render(request, 'login_admin.html')
'''

def cadastro_page(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('namecompleto')
        mae = request.POST.get('nomemae')
        nascimento = request.POST.get('datanascimento')
        naturalidade = request.POST.get('naturalidade')
        cpf =  request.POST.get('cpf')
        rg =  request.POST.get('rg')
        email =  request.POST.get('email')
        password =  request.POST.get('senha')
        dados = Dados_usuario()
        dados.nome = nome
        dados.mae = mae
        dados.nascimento = nascimento
        dados.naturalidade = naturalidade
        dados.cpf = cpf
        dados.rg = rg
        dados.email = email
        dados.password = password
        dados.save()
        return HttpResponseRedirect('/vision_user')
    else:
        return HttpResponseBadRequest()


def vision_user_page(request):
    return render(request, 'vision_user.html')

def vision_admin_page(request):
    return render(request, 'vision_admin.html')