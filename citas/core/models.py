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

    opcionesEstadoCivil = [
        ('SOLTERO', 'SOLTERO'),
        ('CASADO', 'CASADO'),
        ('VIUDO', 'VIUDO'),
        ('DIVORCIADO', 'DIVORCIADO'),
        ('COMPLICADO', 'COMPLICADO'),
        ('NO_ESPECIFICA', 'NO_ESPECIFICA'),
    ]

    personaEstadoCivil = models.CharField(
        choices=opcionesEstadoCivil,
        db_column='estado_civil',
        # si no se proporciona un valor inicial, entonces este sera el vaor por defecto
        default='NO_ESPECIFICA',
        max_length=50
    )

    # ImageField > sirve para almacenar imagenes, PERO solamente guardara en la bd su ubicacion del archivo, y el archivo como tal lo guardara en el proyecto
    personaFoto = models.ImageField(
        db_column='foto',
        # Esta es la carpeta donde se almacenará estos archivos ddentro del proyecto
        upload_to='personas/',
        null=True,
    )

    # Sirve para pasar metadata al padre, a la configuracion del modelo (Model)
    class Meta:
        db_table = 'personas'  # conesto modificaremos el nombre con el que se guardara en la bd
        # ascendente SELECT * ..... ORDER BY email DESC, apellido ASC
        # ordering = ['-email', 'apellido']
        # index_together sirve para crear una clausula unica e irrepetible entre dos o mas columnas.
        # index_together = [['nombre', 'email'], ['nombre', 'apellido', 'estado_civil']]


class CitaModel(models.Model):
    opcionesEstado = [
        ('ACTIVA', 'ACTIVA'),
        ('CANCELADA', 'CANCELADA'),
        ('POSPUESTA', 'POSPUESTA'),
    ]

    # Un autofield vendria a ser un campo entero autoincrementable.
    #  NOTA: solamente puede haber como maximo un autofield por tabla
    citaId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='id')

    citaDescripcion = models.TextField(
        db_column='descripcion',
        null=False,
    )

    citaFecha = models.DateTimeField(
        db_column='fecha',
        null=False,
    )

    citaLatitud = models.FloatField(
        db_column='latitud',
        null=False,
    )

    citaLongitud = models.FloatField(
        db_column='longitud',
        null=False,
    )

    citaEstado = models.CharField(
        choices=opcionesEstado,
        db_column='estado',
        null=False,
        max_length=50
    )
    # campos que registran la fecha de manera automatica cuando se crea un nuevo registro y cuando se actualiza un registro > campos de auditoria o audit fields

    createAd = models.DateTimeField(
        auto_now_add=True,  # agarrara la hora y fecha actual de la bd y pondra ese valor en este campo de manera automatica cuando se cree un nuevo registro
        db_column='created_at'
    )
    updateAt = models.DateTimeField(
        auto_now=True,   # Se modificara el valor cada vez que se haga una modificacion en alguna columna del registro, la que sea y le modificara con su valor actual de la hora y fecha de la bd
        db_column='updated_at'
    )

    # ahora creamos relaciones
    # https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/
    # on_delete: Que se va a suceder cuando se elimite el padre (el citador)
    # CASCADE > Es que primero se elimina el citador y luego se eliminan las citas
    # PROTECT > protegera la eliminacion e indicar que no se puede por lo que manualmente tendremos que eliminar las citas para luego eliminar el citador
    # SET_NULL > eliminar a la persona y en su citas pondra el valor de null
    # DO_NOTHING > permite la eliminacion pero no hace nada en la columna fk, esto genera una mala integridad de los datos ya que tendremos informacion apuntando a personas que no existen
    # RESTRICT > no permite la eliminacion como el PROTECT pero lanzara un error de tipo restrictec
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#arguments

    citador = models.ForeignKey(
        to=PersonaModel,
        db_column='citador_id',
        on_delete=models.PROTECT,
        # servira para ingresar desde la persona a las citas, se usa para las relaciones inversas (inverse relations), si no se declara DJANGO pondra un valor diferente
        related_name='personaCitas'
    )

    citado = models.ForeignKey(
        to=PersonaModel,
        db_column='citado_id',
        on_delete=models.PROTECT,
        related_name='personaCitadas'
    )

    class Meta:
        # La tabla se llame citas
        db_table = 'citas'
        # La fecha debe ser unica con el citador
        # La fecha debe ser unica con el citado

        unique_together = [['citaFecha', 'citador'],
                           ['citaFecha', 'citado']]
        # Su ordenamiento sea por la fecha mas proxima (des)
        ordering = ['-citaFecha']
