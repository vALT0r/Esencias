# Generated by Django 2.0.5 on 2018-08-23 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esencias', '0037_esencia_efecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esencia',
            name='Efecto',
            field=models.CharField(choices=[('Desconocido', 'Desconocido'), ('Sedativa', 'Sedativa'), ('Activadora', 'Activadora'), ('Ambas', 'Ambas')], default='D', max_length=12),
        ),
    ]
