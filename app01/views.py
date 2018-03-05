# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from app01 import models
from app01.models import ClassNum, Course, Teacher, Student


def home(request):
    return HttpResponse('app01_home')


def book(request):
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
    userobjs=models.Author.objects.all()#查找全部
    book_list=models.Book.objects.all().select_related("author").values("name",'author__first_name',"author__last_name","publish__name","date")
    for item in book_list:
        print (item)

    #反向查找

    """
        一对多正向查找，筛选关联表条件或者获取关联表字段 统一使用 外键字段__字段名
        反向查找 筛选关联表条件或者获取关联表字段 统一只用  表名__字段名
    """
    obj_publish=models.Publish.objects.filter(name='美国加州出版社').first()
    print(obj_publish.address)
    print(obj_publish.book_set.all())
    # for item in userlist:
    #     print(item.username,item.password,item.age)
    return render(request,"app01/userlist.html",{"userlist":userobjs,"booklist":book_list})

def AddClass(request):

    #添加班级信息 bulk_create(列表（元素为对象）)批量添加数据
    clss1=ClassNum(caption="一年一班")
    clss2=ClassNum(caption="一年二班")
    clss3=ClassNum(caption="一年三班")
    clss4=ClassNum(caption="一年四班")
    dic=[clss1,clss2,clss3,clss4]
    # dic={{"caption":"一年一班"},{"caption":"一年二班"},{"caption":"一年三班"},{"caption":"一年四班"}}
    models.ClassNum.objects.bulk_create(dic)
    # models.ClassNum.objects.all().delete()
    return HttpResponse("ok")
def addCourse(request):
    # 添加班级信息 bulk_create(列表（元素为对象）)批量添加数据
    c1 = Course(name="数学")
    c2 = Course(name="语文")
    c3 = Course(name="英语")
    c4 = Course(name="科学")
    dic = [c1, c2, c3, c4]
    # dic={{"caption":"一年一班"},{"caption":"一年二班"},{"caption":"一年三班"},{"caption":"一年四班"}}
    models.Course.objects.bulk_create(dic)
    # models.ClassNum.objects.all().delete()
    return HttpResponse("ok")


def addTeacher(request):
    t1=Teacher(username="李阳",age=25,course_id=models.Course.objects.get(name="数学").id)
    t2=Teacher(username="张扬",age=28,course_id=models.Course.objects.get(name="语文").id)
    t3=Teacher(username="李伟",age=27,course_id=models.Course.objects.get(name="英语").id)
    t4=Teacher(username="Alex",age=23,course_id=models.Course.objects.get(name="数学").id)
    # clss1 = models.ClassNum.objects.get(caption="一年一班")
    # clss3 = models.ClassNum.objects.get(caption="一年三班")
    # clss4 = models.ClassNum.objects.get(caption="一年四班")
    # t1.clzz.add(clss1.id)
    # t1.clzz.add(clss1.id)
    # t2.clzz.add(clss1.id)
    # t2.clzz.add(clss3.id)
    # t2.clzz.add(clss4.id)
    # t4.clzz.add(clss3.id)
    # t4.clzz.add(clss4.id)
    l=[t1,t2,t3,t4]
    models.Teacher.objects.bulk_create(l)
    # models.Teacher.objects.all().delete()
    return HttpResponse("ok")

def add_teacher_clzz(request):
    t1 = models.Teacher.objects.get(username="李阳")
    t2 = models.Teacher.objects.get(username="张扬")
    t3 = models.Teacher.objects.get(username="李伟")
    t4 = models.Teacher.objects.get(username="Alex")
    clss1 = models.ClassNum.objects.get(caption="一年一班")
    clss3 = models.ClassNum.objects.get(caption="一年三班")
    clss4 = models.ClassNum.objects.get(caption="一年四班")
    t1.clzz.add(clss1)
    t1.clzz.add(clss1)
    t2.clzz.add(clss1)
    t2.clzz.add(clss3)
    t2.clzz.add(clss4)
    t4.clzz.add(clss3)
    t4.clzz.add(clss4)
    return HttpResponse("ok")

def addStudent(request):
    t1 = Student(name="小明",clzz_id=models.ClassNum.objects.get(caption="一年一班").id)
    t2 = Student(name="小红", clzz_id=models.ClassNum.objects.get(caption="一年一班").id)
    t3 = Student(name="笑话", clzz_id=models.ClassNum.objects.get(caption="一年二班").id)
    t4 = Student(name="小星", clzz_id=models.ClassNum.objects.get(caption="一年三班").id)
    l = [t1, t2, t3, t4]
    models.Student.objects.bulk_create(l)

    return HttpResponse("ok")

def delClass(request):
    models.ClassNum.objects.get(caption="一年三班").delete()

    return HttpResponse("ok")