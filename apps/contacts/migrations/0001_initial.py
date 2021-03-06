# Generated by Django 3.2.9 on 2021-11-23 22:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nombre', max_length=50)),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'db_table': 'grupos',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nombre', max_length=50)),
                ('email', models.EmailField(db_column='email', max_length=254, unique=True)),
                ('phone', models.CharField(db_column='telefono', max_length=16, unique=True, validators=[django.core.validators.RegexValidator(message='Ingrese un número de teléfono válido.', regex='^\\+?1?\\d{8,15}$')])),
                ('group', models.ForeignKey(db_column='grupo', on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='contacts.group')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'db_table': 'contactos',
            },
        ),
    ]
