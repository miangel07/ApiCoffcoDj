# Generated by Django 5.0.4 on 2024-05-15 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquilerLaboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquilerlaboratorio',
            name='fecha_alquiler',
            field=models.DateTimeField(),
        ),
    ]