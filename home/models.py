from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Utilizador(models.Model):
    user = models.OneToOneField(User)
    NIF = models.IntegerField(null=True)
    contacto = models.IntegerField(null=True)
    codigopostal = models.IntegerField(null=True)
    morada = models.CharField(max_length=200, null=True)
    localidade = models.CharField(max_length=50, null=True)
    pais = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username
