from django.db import models
from django.contrib.auth.models import User

CAMPUS = {
    0: 'UFMT - Campus Araguaia',
    1: 'UFMT - Campus Cuiabá',
    2: 'UFMT - Campus Sinop'
}

CURSO = {
    0: 'Agronomia',
    1: 'Ciência da Computação',
    2: 'Engenharia da Computação',
    3: 'Física',
    4: 'Geografia',
    5: 'História',
    6: 'Letras',
    7: 'Matemáica',
    8: 'Medicina'
}

class Estudante(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=20, unique=True)
    nascimento = models.DateField()
    naturalidade = models.CharField(max_length=200)
    mae = models.CharField(max_length=200)
    rg = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    status = models.IntegerField(choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Negado')], default=0)
    campus = models.IntegerField(choices=[(i, nome) for i, nome in CAMPUS.items()], default=0)
    curso = models.IntegerField(choices=[(i, nome) for i, nome in CURSO.items()], default=0)
    
      
'''
class Campus(models.Model):
    pass

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
'''