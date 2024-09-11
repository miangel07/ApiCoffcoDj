# Generated by Django 5.0.4 on 2024-09-11 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo_documento', '0001_initial'),
        ('tipo_servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_carga', models.DateField(null=True)),
                ('codigo_documento', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_Emision', models.DateField(null=True)),
                ('fkTipoDocumentos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tipo_documento.tipo_documento')),
                ('fk_tipoServicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tipo_servicios.tiposervicio')),
            ],
        ),
    ]
