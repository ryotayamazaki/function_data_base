# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 08:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='puroglammei')),
                ('parent', models.CharField(max_length=255, verbose_name='oya')),
                ('maker', models.CharField(max_length=255, verbose_name='sakuseisya')),
                ('mightiness', models.CharField(blank=True, max_length=255, verbose_name='kinou')),
                ('tag', models.CharField(max_length=255, verbose_name='tag')),
                ('git', models.CharField(max_length=255, verbose_name='git')),
            ],
        ),
        migrations.CreateModel(
            name='pkg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='pkgmei')),
                ('child', models.CharField(max_length=255, verbose_name='ko')),
                ('maker', models.CharField(max_length=255, verbose_name='sakuseisya')),
                ('mightiness', models.CharField(blank=True, max_length=255, verbose_name='kinou')),
                ('tag', models.CharField(max_length=255, verbose_name='tag')),
                ('git', models.CharField(max_length=255, verbose_name='git')),
            ],
        ),
        migrations.CreateModel(
            name='Proglam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='puroglammei')),
                ('parent', models.CharField(max_length=255, verbose_name='oya')),
                ('child', models.CharField(max_length=255, verbose_name='ko')),
                ('maker', models.CharField(max_length=255, verbose_name='sakuseisya')),
                ('mightiness', models.CharField(blank=True, max_length=255, verbose_name='kinou')),
                ('tag', models.CharField(max_length=255, verbose_name='tag')),
                ('git', models.CharField(max_length=255, verbose_name='git')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proglam', to='data_base.pkg', verbose_name='pkg')),
            ],
        ),
        migrations.AddField(
            model_name='function',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='function', to='data_base.Proglam', verbose_name='proglam'),
        ),
    ]
