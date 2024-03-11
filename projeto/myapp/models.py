from django.db import models
from django.contrib.auth.models import User


class Estudante(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=20, unique=True)
    nascimento = models.DateField()
    naturalidade = models.CharField(max_length=200)
    mae = models.CharField(max_length=200)
    rg = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
      
      
'''class Estudante(models.Model):
    id = models.AutoField(primary_key=True)
    imagem = models.ImageField(upload_to='images/', null=True, default=None)
'''