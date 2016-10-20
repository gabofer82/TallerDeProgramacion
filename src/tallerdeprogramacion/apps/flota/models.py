from django.db import models


class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10)
    externo = models.BooleanField(default=False)
    # si es una empresa que no pertenece al grupo

    def __str__(self):
        return '{}, {}'.format(self.nombre, self.telefono)


class Coche(models.Model):
    numero = models.CharField(max_length=4)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    año = models.CharField(max_length=4)
    # capacidad = models.SmallIntegerField()
    # estado = models.TimeField()
    propietario = models.ForeignKey(Propietario)
    ventanillas = models.SmallIntegerField()
    pasillos = models.SmallIntegerField()
    ventanillas_ocupadas = models.SmallIntegerField()
    pasillos_ocupados = models.SmallIntegerField()

    @property
    def capacidad(self):
        return self.ventanillas + self.pasillos

    def __str__(self):
        return 'Coche nro: {} - {}, {}'.format(self.numero, self.marca,
            self.modelo)
