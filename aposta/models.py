import datetime
from django.db import models
from django.utils import timezone

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

class Concurso2(models.Model):
    concurso_edicao = models.CharField(max_length=20)
    pub_data = models.DateTimeField('data de publicacao')
    def __str__(self):
        return self.concurso_edicao
    def foi_publicada_recentemente(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)

class Aposta2(models.Model):
    Concurso2_identificao = models.ForeignKey(Concurso2, on_delete=models.CASCADE)
    aposta_identificacao = models.CharField(max_length=200)
    valor = models.IntegerField(default=0)

    def __str__(self):
        return self.aposta_identificacao