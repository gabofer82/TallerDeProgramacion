from django.db import models


class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    externo = models.BooleanField(default=False)
    # si es una empresa que no pertenece al grupo

    def __str__(self):
        return '{}, {}'.format(self.nombre, self.telefono)


class ProporcionAsientos(models.Model):
    ventanillas = models.SmallIntegerField()
    pasillos = models.SmallIntegerField()


class Coche(models.Model):
    numero = models.CharField(max_length=4)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    año = models.CharField(max_length=4)
    capacidad = models.SmallIntegerField()
    estado = models.TimeField()
    propietario = models.ForeignKey(Propietario)
    asientos = models.ForeignKey(ProporcionAsientos)

    def __str__(self):
        return 'Coche nro: {} - {}, {}'.format(self.numero, self.marca,
            self.modelo)
