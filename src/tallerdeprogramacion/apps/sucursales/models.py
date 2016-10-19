from django.db import models


class Sucursal(models.Model):
    direccion = models.CharField(max_length=60)
    pisos = models.CharField(max_length=2)
    localidad = models.ForeignKey(Localidad)

    def __str__(self):
        return '{}, {}'.format(self.localidad, self.direccion)


class Telefono(models.Model):
    numero = models.CharField(max_length=12)
    local = models.IntegerField(Sucursal)

    def __str__(self):
        return 'Telefono bro.: {}'.format(self.numero)


class Parada(models.Model):
    direccion = models.Model(max_length=60)
    localidad = models.ForeignKey(Localidad)

    def __str__(self):
        return 'Parada: {}, {}'.format(self.localidad, self.direccion)


class Departamento(model.Model):
    nombre = models.Model(max_length=30)

    def __str__(self):
        return 'Departamento: {}'.format(self.nombre)


class Localidad(models.Model):
    TIPO = (
        ('V', 'villa',),
        ('P', 'pueblo',),
        ('C', 'ciudad',),
    )
    nombre = models.Model(max_length=30)
    tipo = models.CharField(max_length=1, choices=TIPO)
    departamento = models.ForeignKey(Departamento)

    def __str__(self):
        return '{}, {}'.format(self.nombre, self.departamento)
