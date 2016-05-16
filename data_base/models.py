from django.db import models

# Create your models here.
from datetime import datetime


class data_basedata(models.Model):
    title = models.CharField(max_length=512)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)


class Pkg(models.Model):
    """pakke-zi"""
    name = models.CharField('pkgmei', max_length=255)
    child = models.CharField('ko', max_length=255, blank=True)
    maker = models.CharField('sakuseisya', max_length=255)
    mightiness = models.TextField('kinou', max_length=255)
    tag = models.CharField('tag', max_length=255, blank=True)
    git = models.CharField('git', max_length=255, blank=True)


class Proglam(models.Model):
    """poroglam"""
    link = models.ForeignKey(Pkg, verbose_name='pkg', related_name='proglams')
    name = models.CharField('puroglammei', max_length=255)
    child = models.CharField('ko', max_length=255, blank=True)
    maker = models.CharField('sakuseisya', max_length=255)
    mightiness = models.TextField('kinou', max_length=255)
    tag = models.CharField('tag', max_length=255, blank=True)
    git = models.CharField('git', max_length=255, blank=True)


class Function(models.Model):
    """kansuu"""
    link = models.ForeignKey(Proglam, verbose_name='proglam', related_name='functions')
    name = models.CharField('puroglammei', max_length=255)
    maker = models.CharField('sakuseisya', max_length=255)
    mightiness = models.TextField('kinou', max_length=255)
    tag = models.CharField('tag', max_length=255, blank=True)
    git = models.CharField('git', max_length=255, blank=True)


    
