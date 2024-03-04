from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest

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
    return render(request, 'cadastro.html')

def vision_user_page(request):
    return render(request, 'vision_user.html')

def vision_admin_page(request):
    return render(request, 'vision_admin.html')