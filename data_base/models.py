from django.db import models

# Create your models here.
from datetime import datetime


class data_basedata(models.Model):
    title = models.CharField(max_length=512)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)


class Pkg(models.Model):
    """pakke-zi"""
    name = models.CharField('パッケージ名', max_length=255)
    child = models.CharField('所属するプログラム', max_length=255, blank=True)
    maker = models.CharField('作成者', max_length=255)
    mightiness = models.TextField('機能', max_length=255)
    tag = models.CharField('タグ', max_length=255, blank=True)
    git = models.CharField('git', max_length=255, blank=True)


class Pkg_updated(models.Model):
    """pkgkopusin"""
    date = models.DateTimeField('更新日時', default=datetime.now)
    link = models.ForeignKey(Pkg, verbose_name='pkg', related_name='pkg_updateds')
    maker = models.CharField('更新者', max_length=255)
    content = models.CharField('更新内容', max_length=255)
    reason = models.CharField('更新理由', max_length=255)
    

class Proglam(models.Model):
    """poroglam"""
    link = models.ForeignKey(Pkg, verbose_name='pkg', related_name='proglams')
    name = models.CharField('プログラム名', max_length=255)
    child = models.CharField('使用している関数', max_length=255, blank=True)
    maker = models.CharField('作成者', max_length=255)
    mightiness = models.TextField('機能', max_length=255)
    tag = models.CharField('タグ', max_length=255, blank=True)
    git = models.CharField('git', max_length=255, blank=True)


class Function(models.Model):
    """kansuu"""
    link = models.ForeignKey(Proglam, verbose_name='proglam', related_name='functions')
    name = models.CharField('関数名', max_length=255)
    maker = models.CharField('作成者', max_length=255)
    mightiness = models.TextField('機能', max_length=255)
    tag = models.CharField('タグ', max_length=255, blank=True)
    git = models.CharField('git', max_length=255, blank=True)


class Proglam_updated(models.Model):
    """pkgkopusin"""
    date = models.DateTimeField('更新日時', default=datetime.now)
    link = models.ForeignKey(Proglam, verbose_name='proglam', related_name='proglam_updateds')
    maker = models.CharField('更新者', max_length=255)
    content = models.CharField('更新内容', max_length=255)
    reason = models.CharField('更新理由', max_length=255)
    

class Function_updated(models.Model):
    """pkgkopusin"""
    date = models.DateTimeField('更新日時', default=datetime.now)
    link = models.ForeignKey(Function, verbose_name='function', related_name='function_updateds')
    maker = models.CharField('更新者', max_length=255)
    content = models.CharField('更新内容', max_length=255)
    reason = models.CharField('更新理由', max_length=255)
    

    
