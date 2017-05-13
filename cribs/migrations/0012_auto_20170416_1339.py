# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cribs', '0011_auto_20170416_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crib',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Address'),
        ),
    ]
