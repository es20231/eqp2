# Generated by Django 4.2.1 on 2023-06-14 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_de_usuario', models.CharField(max_length=20)),
                ('nome_completo', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=20)),
                ('descricao_de_perfil', models.CharField(max_length=1000)),
            ],
        ),
    ]
