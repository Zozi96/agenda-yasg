from django.db import models
from django.core import validators


class Group(models.Model):
    """Grupos de contactos"""
    name = models.CharField(
        max_length=50,
        db_column='nombre',
        verbose_name='Nombre del grupo',
    )

    class Meta:
        db_table = 'grupos'
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'

    def __str__(self):
        return self.name


class Contact(models.Model):
    """ Modelo de contacto """

    # Validacion para numeros de telefono
    phone_validator = validators.RegexValidator(
        regex=r"^\+?1?\d{8,15}$",
        message='Ingrese un número de teléfono válido.'
    )

    name = models.CharField(
        max_length=50,
        db_column='nombre',
        verbose_name='Nombre',
    )
    email = models.EmailField(
        max_length=254,
        db_column='email',
        verbose_name='Correo electrónico',
        unique=True,
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=16,
        db_column='telefono',
        verbose_name='Teléfono',
        validators=(phone_validator,),
        unique=True,
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        db_column='grupo',
        verbose_name='Grupo',
        related_name='contacts',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'contactos'
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'

    def __str__(self):
        return self.name
