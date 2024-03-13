import uuid
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from .models import Estudante
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def index(request):
    return HttpResponseRedirect('/plataform')

def plataform_page(request):
    return render(request, 'plataform.html')

@login_required(login_url='/login_user')
def cad_admin_page(request):
    if not request.user.is_staff:
        return HttpResponse('Você precisa estar logado como usuário staff para cadastrar um administrador')
    
    if request.method == 'GET':
        return render(request, 'cad_admin.html')
    elif request.method == 'POST':
        nome = request.POST.get('nomeadmin')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(cpf, email, password)
        user.first_name = nome
        user.save()
        print(nome, cpf, email)
        return HttpResponseRedirect('/vision_admin')
    else:
        return HttpResponseBadRequest()

def login_user_page(request):
    if request.method == 'GET':
        return render(request, 'login_user.html',{
            'incorrect_login' : False
        })
    elif request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('senha')
        user = authenticate(request, username=cpf, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/vision_user')
        else:
            return render(request, 'login_user.html', {
                'incorrect_login' : True
            })
    else:
        return HttpResponseBadRequest()
    

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
        campus = request.POST.get('instituicao')
        curso = request.POST.get('curso')
        email =  request.POST.get('email')
        password =  request.POST.get('senha')
        user = User.objects.create_user(cpf, email, password)
        user.first_name = nome
        user.save()
        print(campus, curso)
        perfil = Estudante()
        perfil.email = email
        perfil.user = user
        perfil.mae = mae
        perfil.nascimento = nascimento
        perfil.naturalidade = naturalidade
        perfil.cpf = cpf
        perfil.rg = rg
        perfil.campus
        perfil.curso
        perfil.save()
        return HttpResponseRedirect('/vision_user')
    else:
        return HttpResponseBadRequest() 

@login_required(login_url='/login_user')
def vision_user_page(request):
    return render(request, 'vision_user.html', {
        'estudante': request.user.estudante
    })

@login_required(login_url='/login_user')
def vision_admin_page(request):
    estudantes = Estudante.objects.all()
    return render(request, 'vision_admin.html', {
        'estudantes' : estudantes
    })
    
def table_page(request):
    return render(request, 'table.html')