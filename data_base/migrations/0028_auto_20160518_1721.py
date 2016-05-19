# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 08:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0027_auto_20160518_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='maker',
            field=models.CharField(max_length=255, verbose_name='作成者'),
        ),
        migrations.AlterField(
            model_name='function',
            name='mightiness',
            field=models.TextField(max_length=255, verbose_name='機能'),
        ),
        migrations.AlterField(
            model_name='function',
            name='name',
            field=models.CharField(max_length=255, verbose_name='関数名'),
        ),
        migrations.AlterField(
            model_name='function',
            name='tag',
            field=models.CharField(blank=True, max_length=255, verbose_name='タグ'),
        ),
        migrations.AlterField(
            model_name='function_updated',
            name='content',
            field=models.CharField(max_length=255, verbose_name='更新内容'),
        ),
        migrations.AlterField(
            model_name='function_updated',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='function_updated',
            name='maker',
            field=models.CharField(max_length=255, verbose_name='更新者'),
        ),
        migrations.AlterField(
            model_name='function_updated',
            name='reason',
            field=models.CharField(max_length=255, verbose_name='更新理由'),
        ),
        migrations.AlterField(
            model_name='pkg',
            name='child',
            field=models.CharField(blank=True, max_length=255, verbose_name='所属するプログラム'),
        ),
        migrations.AlterField(
            model_name='pkg',
            name='maker',
            field=models.CharField(max_length=255, verbose_name='作成者'),
        ),
        migrations.AlterField(
            model_name='pkg',
            name='mightiness',
            field=models.TextField(max_length=255, verbose_name='機能'),
        ),
        migrations.AlterField(
            model_name='pkg',
            name='name',
            field=models.CharField(max_length=255, verbose_name='パッケージ名'),
        ),
        migrations.AlterField(
            model_name='pkg',
            name='tag',
            field=models.CharField(blank=True, max_length=255, verbose_name='タグ'),
        ),
        migrations.AlterField(
            model_name='pkg_updated',
            name='content',
            field=models.CharField(max_length=255, verbose_name='更新内容'),
        ),
        migrations.AlterField(
            model_name='pkg_updated',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='pkg_updated',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pkg_updateds', to='data_base.Pkg', verbose_name='pkg'),
        ),
        migrations.AlterField(
            model_name='pkg_updated',
            name='maker',
            field=models.CharField(max_length=255, verbose_name='更新者'),
        ),
        migrations.AlterField(
            model_name='pkg_updated',
            name='reason',
            field=models.CharField(max_length=255, verbose_name='更新理由'),
        ),
        migrations.AlterField(
            model_name='proglam',
            name='child',
            field=models.CharField(blank=True, max_length=255, verbose_name='使用している関数'),
        ),
        migrations.AlterField(
            model_name='proglam',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proglams', to='data_base.Pkg', verbose_name='pkg'),
        ),
        migrations.AlterField(
            model_name='proglam',
            name='maker',
            field=models.CharField(max_length=255, verbose_name='作成者'),
        ),
        migrations.AlterField(
            model_name='proglam',
            name='mightiness',
            field=models.TextField(max_length=255, verbose_name='機能'),
        ),
        migrations.AlterField(
            model_name='proglam',
            name='name',
            field=models.CharField(max_length=255, verbose_name='プログラム名'),
        ),
        migrations.AlterField(
            model_name='proglam',
            name='tag',
            field=models.CharField(blank=True, max_length=255, verbose_name='タグ'),
        ),
        migrations.AlterField(
            model_name='proglam_updated',
            name='content',
            field=models.CharField(max_length=255, verbose_name='更新内容'),
        ),
        migrations.AlterField(
            model_name='proglam_updated',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='proglam_updated',
            name='maker',
            field=models.CharField(max_length=255, verbose_name='更新者'),
        ),
        migrations.AlterField(
            model_name='proglam_updated',
            name='reason',
            field=models.CharField(max_length=255, verbose_name='更新理由'),
        ),
    ]
