from django.db import models
#apuntar chuleta:
from django.db.models import Q
from django.conf import settings

# Create your models here.
class Artista(models.Model):
    class Genero(models.TextChoices):
        POP = "POP", "Pop"
        ROCK = "ROCK","Rock"
        JAZZ = "JAZZ","Jazz"

    nombre = models.CharField(max_length=100, unique=True)
    pais = models.CharField(max_length=100)
    genero_musical = models.CharField(max_length=5,choices=Genero.choices,default=Genero.POP)
    fehca_creacion = models.DateField()
    cache = models.DecimalField(max_digits=8,decimal_places=2)
    activo = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(cache__gte=0),
                name="cache_mayor_0"
            )
        ]

    def __str__(self):
        return self.nombre

class Escenario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ubicacion = models.CharField(max_length=100)
    aforo = models.DecimalField(max_digits=8,decimal_places=2)
    cubierto = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(aforo__gt=0),
                name="aforo_mayor_0"
            )
        ]

    def __str__(self):
        return self.nombre

class Concierto(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()
    duracion = models.DecimalField(max_digits=8,decimal_places=2)
    precio = models.DecimalField(max_digits=8,decimal_places=2)
    escenario = models.ForeignKey(Escenario, on_delete=models.PROTECT, related_name="conciertos", null=False,blank=False)
    artistas = models.ManyToManyField(Artista, related_name="conciertos",null=True, blank=True)
    entradas_disponibles = models.DecimalField(max_digits=8,decimal_places=2)
    cancelado = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(duracion__gt=0),
                name="duracion_mayor_0"
            ),
            models.CheckConstraint(
                condition=Q(precio__gte=0),
                name="precio_mayor_0"
            )
        ]

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="perfil_usuario"
    )
    dni = models.CharField(max_length=100,unique=True)
    telefono = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    localidad = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario

class Reserva(models.Model):
    class Estado(models.TextChoices):
        CONFIRMADA = "CONF", "Confirmada"
        CANCELADA = "CANC", "Cancelada"

    localizador = models.CharField(max_length=100,unique=True)
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE,related_name="reservas", null=True, blank=True)
    concierto = models.ForeignKey(Concierto, on_delete=models.PROTECT,related_name="reservas",null=True, blank=True)
    fecha_reserva = models.DateField()
    numero_entradas = models.DecimalField(max_digits=8,decimal_places=2)
    importe_total = models.DecimalField(max_digits=8,decimal_places=2)
    estado = models.CharField(max_length=4, choices=Estado.choices, default=Estado.CONFIRMADA)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(numero_entradas__gt=0),
                name="entrada_mayor_0"
            )
        ]

    def __str__(self):
        return self.localizador