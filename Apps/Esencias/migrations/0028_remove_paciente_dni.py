# Generated by Django 2.0.5 on 2018-07-28 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Esencias', '0027_auto_20180725_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='DNI',
        ),
    ]
