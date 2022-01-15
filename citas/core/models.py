from pyexpat import model
from django.db import models

# Create your models here.


class PersonaModel(models.Model):
    personaId = models.AutoField(
        primary_key=True,  # indica que esta columna sera la primary jey de la tabla
        unique=True,  # indica que no puede tener valores repetidos
        null=False,  # indica que no puede tener valor alguno
        db_column='id')  # indica el nombre que llevara en la tabla en la bd

    personaNombre = models.CharField(
        max_length=50,  # que almacenara como maximo 50 caracteres
        unique=False,
        null=False,
        # sdb_colum='nombre'. Si no le indicamos, entonces su nombre sera el mismo que el atributi (personaNombre)
        db_column='nombre')

    personaApellido = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='apellido')

    personaEmail = models.EmailField(
        max_length=50,
        unique=True,
        null=False,
        db_column='email')

    personaFechaNacimiento = models.DateField(
        db_column='fec_nac',
    )

    opcionesEstadoCivil = [{
        ('SOLTERO', 'SOLTERO')
        ('CASADO', 'CASADO')
        ('VIUDO', 'VIUDO')
        ('DIVORCIADO', 'DIVORCIADO')
        ('COMPLICADO', 'COMPLICADO')
        ('NO_ESPECIFICA', 'NO_ESPECIFICA')
    }]

    personaEstadoCivil = models.CharField(
        choices=opcionesEstadoCivil,
        db_column='estado_civil',
        # si no se proporciona un valor inicial, entonces este sera el vaor por defecto
        default='NO_ESPECIFICA',
    )

    # ImageField > sirve para almacenar imagenes, PERO solamente guardara en la bd su ubicacion del archivo, y el archivo como tal lo guardara en el proyecto
    personaFoto = models.ImageField(
        db_colum='foto',
        # Esta es la carpeta donde se almacenará estos archivos ddentro del proyecto
        upload_to='personas/',
        null=True,
    )
