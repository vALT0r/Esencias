# Generated by Django 2.0.5 on 2018-08-03 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esencias', '0029_paciente_recomendado'),
    ]

    operations = [
        migrations.AddField(
            model_name='esencia',
            name='PlusInfo',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
