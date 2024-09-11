# Generated by Django 5.0.4 on 2024-09-11 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('precios', '0001_initial'),
        ('servicio', '0001_initial'),
        ('tipo_servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preciosmodels',
            name='servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicio.servicio'),
        ),
        migrations.AddField(
            model_name='preciosmodels',
            name='tipoServicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tipo_servicios.tiposervicio'),
        ),
    ]
