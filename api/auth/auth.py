# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/21
@Author: Zhang Yafei
"""
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models


class LuffyAuth(BaseAuthentication):

    def authenticate(self, request):
        token = request.query_params.get('token')
        obj = models.UserAuthToken.objects.filter(token=token).first()
        if not obj:
            raise AuthenticationFailed({'code':1001,'error':'认证失败'})
        return (obj.user.username, obj)