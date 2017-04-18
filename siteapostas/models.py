import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


class Concurso(models.Model):
    edicao = models.CharField(max_length=20)
    pub_data = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.edicao

class Aposta(models.Model):
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE)
    aposta_chave = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.opcao_texto
