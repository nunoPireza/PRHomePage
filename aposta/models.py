import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Conta(models.Model):
    numConta = models.IntegerField
    saldo = models.IntegerField
    nomeUtilizador = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    def __str__(self):
        return self.numConta

class Concurso(models.Model):
    numConcurso = models.SmallIntegerField(primary_key=True)
    dataConcurso = models.DateTimeField('dataconcurso')
    b1 = models.CharField(max_length=2)
    b2 = models.CharField(max_length=2)
    b3 = models.CharField(max_length=2)
    b4 = models.CharField(max_length=2)
    b5 = models.CharField(max_length=2)
    e1 = models.CharField(max_length=2)
    e2 = models.CharField(max_length=2)
    def __str__(self):
        return self.numConcurso

class Aposta(models.Model):
    nAposta = models.SmallIntegerField(primary_key=True)
    nConta = models.IntegerField(null=True)
    dataAposta = models.DateField()
    nome = models.CharField(max_length=200)
    b1 = models.CharField(max_length=2)
    b2 = models.CharField(max_length=2)
    b3 = models.CharField(max_length=2)
    b4 = models.CharField(max_length=2)
    b5 = models.CharField(max_length=2)
    e1 = models.CharField(max_length=2)
    e2 = models.CharField(max_length=2)

    def __str__(self):
        return self.nAposta
