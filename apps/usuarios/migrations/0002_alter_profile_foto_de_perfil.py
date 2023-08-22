from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto_de_perfil',
            field=models.ImageField(default='static/resources/default.jpg', upload_to='static/media/fotos_de_perfil'),
        ),
    ]
