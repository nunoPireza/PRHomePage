# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numConta', models.IntegerField(null=True)),
                ('numConcurso', models.IntegerField(null=True)),
                ('data_aposta', models.DateTimeField(verbose_name='dataaposta')),
                ('chaveB1', models.CharField(max_length=2)),
                ('chaveB2', models.CharField(max_length=2)),
                ('chaveB3', models.CharField(max_length=2)),
                ('chaveB4', models.CharField(max_length=2)),
                ('chaveB5', models.CharField(max_length=2)),
                ('chaveE1', models.CharField(max_length=2)),
                ('chaveE2', models.CharField(max_length=2)),
            ],
        ),
    ]