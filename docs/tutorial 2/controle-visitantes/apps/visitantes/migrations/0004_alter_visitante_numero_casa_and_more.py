# Generated by Django 4.2.1 on 2023-06-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0003_visitante_placa_veiculo_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitante',
            name='numero_casa',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número da casa a ser visitada'),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='placa_veiculo_foto',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='uploads/', verbose_name='Foto da placa do veículo'),
        ),
    ]
