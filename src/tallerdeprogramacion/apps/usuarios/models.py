from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User)
    domicilio = models.CharField(max_length=80)
    telefono = models.CharField(max_length=12)
    celular = models.CharField(max_length=9)


def creador_perfil(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)


post_save.connect(creador_perfil, sender=User)
