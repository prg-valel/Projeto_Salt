# Generated by Django 5.0.3 on 2024-03-08 12:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_perfil_role'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perfil',
            new_name='Estudante',
        ),
    ]
