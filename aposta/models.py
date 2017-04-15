from django.db import models

# Create your models here.

class Conta(models.Model):
    numConta = models.IntegerField

class Concurso(models.Model):
    numConcurso = models.IntegerField

class Aposta(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE)
    dataAposta = models.DateTimeField()