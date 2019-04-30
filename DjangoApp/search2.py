#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      search2
   Description :
   Author :         0049003013
   date：           2019/4/29
-------------------------------------------------
   Change Activity: 2019/4/29:
-------------------------------------------------
"""


from django.shortcuts import render
from django.views.decorators import csrf

def search_post(request):
    ctx={}
    if request.POST:
        ctx['rlt']=request.POST['q']
    return render(request, "post.html", ctx)