# Generated by Django 5.0.4 on 2024-09-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VariblesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreVaribles', models.CharField(max_length=500)),
                ('estadovarible', models.CharField(choices=[('activo', 'activo'), ('inactivo', 'inactivo')], default='activo', max_length=20)),
                ('tipo_Dato', models.CharField(choices=[('text', 'Texto'), ('number', 'Numero'), ('date', 'Fecha')], max_length=20)),
            ],
        ),
    ]