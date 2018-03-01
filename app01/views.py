# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from app01 import models


def home(request):
    return HttpResponse('app01_home')


def adduser(request):
    """

       :param request: request.POST 获取post方式传递的数据 GET 获取get方式传递的数据
       :return:
       """
    # 增加用户
    # dic = {"username": "朱国庆", "password": "zhuguoqing", "age": 27}
    # models.UserInfo.objects.create(username="alex",password="alex",age=24)
    # models.UserInfo.objects.create(**dic)
    #修改 1、首先要先找到要修改的数据 通过 filter方法

    # models.UserInfo.objects.filter(username="alex").update(password="123456")

    #删除
    # models.UserInfo.objects.filter(username="alex").delete()

    #查找 查找的列表是QuerySet类型
    userobjs=models.UserInfo.objects.all()#查找全部
    # for item in userlist:
    #     print(item.username,item.password,item.age)
    return render(request,"app01/userlist.html",{"userlist":userobjs})
