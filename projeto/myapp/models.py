from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    ROLE_CHOICES = (
        (1, 'Administrador'),
        (2, 'Aluno'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICES, blank=True, null=True)
      
      
'''class Estudante(models.Model):
    id = models.AutoField(primary_key=True)
    imagem = models.ImageField(upload_to='images/', null=True, default=None)
'''
class Dados_usuario(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=200)
    nascimento = models.DateField()
    naturalidade = models.TextField()
    mae = models.TextField()
    rg = models.IntegerField()
    email = models.TextField()
    