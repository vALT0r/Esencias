# Generated by Django 2.0.5 on 2018-07-05 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Esencias', '0023_auto_20180705_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formula',
            name='Imagen',
        ),
    ]