#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      testDb
   Description :
   Author :         0049003013
   date：           2019/4/29
-------------------------------------------------
   Change Activity: 2019/4/29:
-------------------------------------------------
"""


from django.http import HttpResponse
from TestModel.models import  Test
def testdb(request):
    # test1=Test(name='runoob')
    # test1.save()
    # return HttpResponse("<p>111</p>")
    response=""
    response1=""
    list=Test.objects.all()
    print(list)
    response2=  Test.objects.filter(id=1)
    response3=Test.objects.get(id=1)
    Test.objects.order_by('name')[0:2]
    Test.objects.order_by("id")
    Test.objects.filter(name="runoob").order_by("id")
    for var in list:
        response1+=var.name+" "
    response=response1
    return HttpResponse("<p>"+response+"</p>")
