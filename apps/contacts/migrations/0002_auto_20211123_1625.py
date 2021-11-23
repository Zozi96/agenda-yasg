# Generated by Django 3.2.9 on 2021-11-23 22:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, db_column='email', max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, db_column='telefono', max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Ingrese un número de teléfono válido.', regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
