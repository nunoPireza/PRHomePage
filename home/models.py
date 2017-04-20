from django.db import models

# Create your models here.

class Aposta(models.Model):
    numConta = models.IntegerField(null=True)
    numConcurso = models.IntegerField(null=True)
    data_aposta = models.DateTimeField('dataaposta')
    chaveB1 = models.CharField(max_length=2)
    chaveB2 = models.CharField(max_length=2)
    chaveB3 = models.CharField(max_length=2)
    chaveB4 = models.CharField(max_length=2)
    chaveB5 = models.CharField(max_length=2)
    chaveE1 = models.CharField(max_length=2)
    chaveE2 = models.CharField(max_length=2)

    def __str__(self):
        return "Aposta: " + self.id

