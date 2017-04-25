# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 18:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIF', models.IntegerField(null=True)),
                ('contacto', models.IntegerField(null=True)),
                ('codigopostal', models.IntegerField(null=True)),
                ('morada', models.CharField(max_length=200, null=True)),
                ('localidade', models.CharField(max_length=50, null=True)),
                ('pais', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]