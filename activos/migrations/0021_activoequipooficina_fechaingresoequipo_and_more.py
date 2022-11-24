# Generated by Django 4.1.1 on 2022-11-20 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0020_alter_activoequipooficina_componentesadicionales'),
    ]

    operations = [
        migrations.AddField(
            model_name='activoequipooficina',
            name='fechaIngresoEquipo',
            field=models.DateField(default=datetime.date.today, help_text='DD/MM/AAAA', verbose_name='Fecha de Ingreso'),
        ),
        migrations.AddField(
            model_name='activoextintor',
            name='fechaIngresoExtintor',
            field=models.DateField(default=datetime.date.today, help_text='DD/MM/AAAA', verbose_name='Fecha de Ingreso'),
        ),
    ]
