# Generated by Django 3.2.20 on 2023-07-26 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0004_alter_profile_foto_de_perfil'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]