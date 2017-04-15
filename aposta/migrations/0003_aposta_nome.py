# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aposta', '0002_remove_aposta_conta'),
    ]

    operations = [
        migrations.AddField(
            model_name='aposta',
            name='nome',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
