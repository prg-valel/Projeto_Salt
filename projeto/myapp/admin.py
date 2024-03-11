from django.contrib import admin
from .models import Estudante

@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    pass
