# Generated by Django 4.1.1 on 2022-11-01 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_usuario_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, default='media/usuarios/default.jpg', upload_to='media/usuarios'),
        ),
    ]
