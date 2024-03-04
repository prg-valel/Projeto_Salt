from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    ROLE_CHOICES = (
        (1, 'Administrador'),
        (2, 'Aluno'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICES, blank=True, null=True)
      
      
class Estudante(models.Model):
    id = models.AutoField(primary_key=True)
    imagem = models.ImageField(upload_to='images/', null=True, default=None)
