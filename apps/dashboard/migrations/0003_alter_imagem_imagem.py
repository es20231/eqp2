# Generated by Django 4.2.3 on 2023-07-26 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_imagem_options_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/galeria'),
        ),
    ]
