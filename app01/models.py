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
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()

