# Generated by Django 3.2.20 on 2023-08-22 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_profile_foto_de_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='descricao_de_perfil',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]