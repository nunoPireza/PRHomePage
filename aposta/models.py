from django.db import models

# Create your models here.
class Conta(models.Model):
    numConta = models.IntegerField
    def __str__(self):
        return self.numConta

class Concurso(models.Model):
    numConcurso = models.IntegerField
    def __str__(self):
        return self.numConcurso

class Aposta(models.Model):
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE)
    dataAposta = models.DateField()
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome