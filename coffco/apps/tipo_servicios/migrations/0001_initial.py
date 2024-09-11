# Generated by Django 5.0.4 on 2024-09-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreServicio', models.CharField(max_length=200)),
                ('estado', models.CharField(choices=[('activo', 'activo'), ('inactivo', 'inactivo')], default='activo', max_length=10)),
            ],
        ),
    ]
