# Generated by Django 2.0.5 on 2018-06-06 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esencias', '0016_auto_20180606_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esencia',
            name='Imagen',
            field=models.CharField(blank=True, max_length=203),
        ),
        migrations.AlterField(
            model_name='esencia',
            name='Negativos',
            field=models.CharField(blank=True, max_length=202),
        ),
        migrations.AlterField(
            model_name='esencia',
            name='Positivos',
            field=models.CharField(blank=True, max_length=201),
        ),
        migrations.AlterField(
            model_name='esencia',
            name='Pregunta1',
            field=models.CharField(blank=True, max_length=204),
        ),
        migrations.AlterField(
            model_name='esencia',
            name='Pregunta2',
            field=models.CharField(blank=True, max_length=205),
        ),
        migrations.AlterField(
            model_name='esencia',
            name='Pregunta3',
            field=models.CharField(blank=True, max_length=206),
        ),
        migrations.AlterField(
            model_name='esencia',
            name='Pregunta4',
            field=models.CharField(blank=True, max_length=207),
        ),
        migrations.AlterField(
            model_name='esencia',
            name='Pregunta5',
            field=models.CharField(blank=True, max_length=208),
        ),
        migrations.AlterField(
            model_name='esencia',
            name='Subtitulo',
            field=models.CharField(blank=True, max_length=199),
        ),
    ]