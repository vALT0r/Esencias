# Generated by Django 2.0.5 on 2018-08-05 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esencias', '0032_auto_20180804_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='Abortos',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Alimentacion',
            field=models.CharField(blank=True, choices=[('M', 'Mala'), ('R', 'Regular'), ('B', 'Buena')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Anemia',
            field=models.CharField(blank=True, choices=[('N', 'No'), ('S', 'Si')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='paciente',
            name='AntecFamilMental',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Constelaciones',
            field=models.CharField(blank=True, choices=[('N', 'No'), ('S', 'Si'), ('U', 'Ultimo Año'), ('M', 'Mas de 1 Año')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='paciente',
            name='DetalleSistemas',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Diabetes',
            field=models.CharField(blank=True, choices=[('N', 'No'), ('S', 'Sin Insulina'), ('C', 'Con Insulina')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='paciente',
            name='EnfermedadesActuales',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='paciente',
            name='EnfermedadesPasadas',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Hermanos',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Hijos',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='paciente',
            name='HoraNacimiento',
            field=models.TimeField(blank=True, default='00:00:00', max_length=60),
        ),
        migrations.AddField(
            model_name='paciente',
            name='LugarNacimiento',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Medicacion',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='paciente',
            name='MotivoVisita',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Observaciones',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Operaciones',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='paciente',
            name='OtrosSistemas',
            field=models.CharField(blank=True, choices=[('N', 'No'), ('S', 'Si')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Pareja',
            field=models.CharField(blank=True, choices=[('N', 'No'), ('S', 'Si')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='paciente',
            name='ParejaTiempo',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Profesion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Yoga',
            field=models.CharField(blank=True, choices=[('N', 'No'), ('S', 'Si'), ('U', 'Ultimo Año'), ('M', 'Mas de 1 Año')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='FechaNacimiento',
            field=models.DateField(blank=True, max_length=60),
        ),
    ]
