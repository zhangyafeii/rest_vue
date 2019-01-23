# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/16
@Author: Zhang Yafei
"""
import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from api import models


class AuthView(APIView):

    # def options(self, request, *args, **kwargs):
    #     # 进行预检
    #     obj = HttpResponse('..')
    #     obj['Access-Control-Allow-Origi'] = '*'
    #     obj['Access-Control-Allow-Headers'] = "Content-Type"
    #
    #     return obj

    def post(self, request, *args, **kwargs):
        # print(request.data)
        ret = {'code': 1000}
        user = request.data.get('user')
        pwd = request.data.get('pwd')

        user = models.Account.objects.filter(username=user, password=pwd).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误'
        else:
            uid = str(uuid.uuid4())
            models.UserAuthToken.objects.update_or_create(user=user, defaults={'token':uid})
            ret['token'] = uid

        return Response(ret)