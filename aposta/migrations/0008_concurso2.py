# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aposta', '0007_auto_20170420_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concurso2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concurso_edicao', models.CharField(max_length=20)),
                ('pub_data', models.DateTimeField(verbose_name='data de publicacao')),
            ],
        ),
    ]