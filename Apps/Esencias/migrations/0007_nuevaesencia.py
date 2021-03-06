# Generated by Django 2.0.5 on 2018-05-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esencias', '0006_subsintoma_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='NuevaEsencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('NombreCientifico', models.CharField(blank=True, max_length=50)),
                ('Subtitulo', models.CharField(blank=True, max_length=200)),
                ('Positivos', models.CharField(blank=True, max_length=100)),
                ('Negativos', models.CharField(blank=True, max_length=100)),
                ('Descripcion', models.CharField(blank=True, max_length=5000)),
                ('TestIntuitivo', models.CharField(blank=True, max_length=1000)),
                ('DescripcionCorta', models.CharField(blank=True, max_length=1000)),
                ('Imagen', models.CharField(blank=True, max_length=200)),
                ('Pregunta1', models.CharField(max_length=200)),
                ('Pregunta2', models.CharField(blank=True, max_length=200)),
                ('Pregunta3', models.CharField(blank=True, max_length=200)),
                ('Pregunta4', models.CharField(blank=True, max_length=200)),
                ('Pregunta5', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
