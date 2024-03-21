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

def visual_page(request, id):
    estudante = Estudante.objects.get(id=id)
    return render(request, 'visual.html', {
        'estudante': estudante
    })

@login_required(login_url='/login_user')
def aprovar(request, id):
    if Estudante.objects.filter(user=request.user).exists():
        return HttpResponseBadRequest()
    estudante = Estudante.objects.get(id=id)
    estudante.status = 1
    estudante.save()
    return HttpResponseRedirect('/vision_admin')


@login_required(login_url='/login_user')
def recad_page(request):
    if request.method == 'GET':
        return render(request, 'recad.html')
    elif request.method == 'POST':
        perfil = Estudante.objects.get(user=request.user)
        perfil.imgrg = request.FILES['imgrg']
        perfil.imgcomp = request.FILES['imgcomp']
        perfil.status = 0
        perfil.save()
        return HttpResponseRedirect('/vision_user') 
    else:
        return HttpResponseBadRequest() 

@login_required(login_url='/login_user')
def negar(request, id):
    if Estudante.objects.filter(user=request.user).exists():
        return HttpResponseBadRequest()
    estudante = Estudante.objects.get(id=id)
    estudante.status = 2
    estudante.save()
    return HttpResponseRedirect('/vision_admin')
    

@login_required(login_url='/login_user')
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/plataform')

def login_admin_page(request):
    if request.method == 'GET':
        return render(request, 'login_admin.html',{
            'incorrect_login' : False
        })
    elif request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('senha')
        user = authenticate(request, username=cpf, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/vision_admin')
        else:
            return render(request, 'login_admin.html', {
                'incorrect_login' : True
            })
    else:
        return HttpResponseBadRequest()


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
        if User.objects.filter(username=cpf).exists():
            mensagem_erro = 'CPF já cadastrado. Por favor, insira um CPF diferente.'
            return render(request, 'cadastro.html', {'mensagem_erro': mensagem_erro})
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
        perfil.campus = campus
        perfil.curso = curso
        perfil.imgrg = request.FILES['imgrg']
        perfil.imgcomp = request.FILES['imgcomp']
        perfil.save()
        return HttpResponseRedirect('/plataform') 
    else:
        return HttpResponseBadRequest() 

@login_required(login_url='/login_user')
def vision_user_page(request):
    if not Estudante.objects.filter(user=request.user).exists():
        return HttpResponse('Você não pode acessar esta página porque não é estudante')
    
    return render(request, 'vision_user.html', {
        'estudante': request.user.estudante
    })

@login_required(login_url='/login_user')
def vision_admin_page(request):
    if Estudante.objects.filter(user=request.user).exists():
        return HttpResponse('Você não pode acessar esta página porque não é administrador')
    
    estudantes_pendentes = Estudante.objects.filter(status=0)
    estudantes_aprovados = Estudante.objects.filter(status=1)
    estudantes_negados = Estudante.objects.filter(status=2)

    return render(request, 'vision_admin.html', {
        'estudantes' : estudantes_pendentes,
        'aprovados' : estudantes_aprovados,
        'negados' : estudantes_negados
    })
    
def table_page(request):
    return render(request, 'table.html')