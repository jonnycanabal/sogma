# Generated by Django 4.1.1 on 2022-11-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionActivos', '0005_registrarmantenimiento_adjuntararchivomantenimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantenimientoextintor',
            name='usado',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=5, verbose_name='¿Extintor usado?'),
        ),
    ]
