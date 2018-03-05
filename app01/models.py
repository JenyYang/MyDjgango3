# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

#
"""
    1、写好类文件
    2、执行python manage.py makemigrations 命令 生成配置文件
    3、执行 python manage.py migrate 命令 生成表
"""
class Course(models.Model):
    """
        科目
    """
    # nid=models.AutoField()
    name=models.CharField(max_length=32)


class ClassNum(models.Model):
    # nid=models.AutoField()
    caption=models.CharField(max_length=64,unique=True)

class Teacher(models.Model):
    """
    教师
    """
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    course=models.ForeignKey(Course)
    clzz=models.ManyToManyField(ClassNum)

class Student(models.Model):
    name=models.CharField(max_length=32,unique=True)
    clzz=models.ForeignKey(ClassNum)



class Author(models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    email=models.EmailField()

    def __unicode__(self):
        return "<%s%s>"%(self.first_name,self.last_name)

class Publish(models.Model):
    name=models.CharField(max_length=128)
    address=models.CharField(max_length=128)
    city=models.CharField(max_length=64)
    state_province=models.CharField(max_length=128)
    country=models.CharField(max_length=32)
    website=models.URLField()

    def __unicode__(self):
        return "<%s>"%(self.name)


class Book(models.Model):
    name=models.CharField(max_length=128)
    author=models.ManyToManyField(Author)
    publish=models.ForeignKey(Publish)
    date=models.DateField()

    def __unicode__(self):
        return "<%s>"%(self.name)


