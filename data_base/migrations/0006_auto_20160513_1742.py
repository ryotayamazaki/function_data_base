# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0005_auto_20160513_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proglam',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proglam', to='data_base.Pkg', verbose_name='pkg'),
        ),
    ]
