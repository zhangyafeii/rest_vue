# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/21
@Author: Zhang Yafei
"""
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


class MYWare(MiddlewareMixin):
    def process_request(self, request):
        print('process request')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('process view')

    def process_exception(self, request, exception):
        print('process exception')

    def process_response(self, request, response):
        print('response')
        return response


class MyWareA(MiddlewareMixin):
    def process_request(self, req):
        print("中间件1的请求")

    def process_response(self, req, response):
        print("中间件1的返回")
        return response

    def process_view(self, req, callback, callback_args, callback_kwargs):
        print("中间件1的view")


class MyWareB(MiddlewareMixin):
    def process_request(self, req):
        print("中间件2的请求")

    def process_response(self, req, response):
        print("中间件2的返回")
        return response

    def process_view(self, req, callback, callback_args, callback_kwargs):
        print("中间件2的view")


class MyWareC(MiddlewareMixin):
    def process_request(self, req):
        print("中间件3的请求")

    def process_response(self, req, response):
        print("中间件3的返回")
        return response

    def process_view(self, req, callback, callback_args, callback_kwargs):
        print("中间件3的view")
