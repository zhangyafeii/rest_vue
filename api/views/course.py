# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/16
@Author: Zhang Yafei
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer,AdminRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from api import models
from rest_framework import serializers
from api.auth.auth import LuffyAuth


class CourseSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = models.Course
        fields = ['id','name', 'course_img', 'sub_category', 'level', 'status']


# class CourseDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CourseDetail
#         fields = '__all__'
#         depth = 1  # 0-10


class CourseDetailSerializer(serializers.ModelSerializer):
    # one2one/fk/choice
    name = serializers.CharField(source='course.name')
    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')

    # m2m
    recommends = serializers.SerializerMethodField()
    chapters = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        fields = ['course', 'name', 'img', 'level','course_slogan', 'why_study', 'career_improvement', 'what_to_study_brief', 'prerequisite', 'recommends', 'chapters', 'teachers']

    def get_recommends(self, obj):
        # 获取所有推荐的课程
        queryset = obj.recommend_courses.all()

        return [{'id':row.id,'title':row.name} for row in queryset]

    def get_chapters(self, obj):
        # 获取指定课程所有章节
        queryset = obj.course.coursechapters.all()

        return [{'id':row.id,'name':row.name} for row in queryset]

    def get_teachers(self, obj):
        # 获取指定课程所有老师
        queryset = obj.teachers.all()

        return [{'id':row.id,'name':row.name} for row in queryset]

# 方式一
# class CourseView(APIView):
#     # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#     # versioning_class = QueryParameterVersioning
#     # versioning_class = URLPathVersioning
#
#     def get(self, request, *args, **kwargs):
#         # ret = {
#         #     'code':1000,
#         #     'data':[
#         #         {'id':1,'title':'Python全栈'},
#         #         {'id':2,'title':'Linux运维'},
#         #         {'id':3,'title':'金融分析'},
#         #     ]
#         # }
#         # return Response(ret)
#         ret = {'code':1000, 'data':None}
#         try:
#             pk = kwargs.get('pk')
#             if pk:
#                 obj = models.Course.objects.filter(id=pk).first()
#                 ser = CourseSerializer(instance=obj,many=False)
#             else:
#                 queryset = models.Course.objects.all()
#                 ser = CourseSerializer(instance=queryset, many=True)
#             ret['data'] = ser.data
#         except Exception:
#             ret['code'] = 1001
#             ret['error'] = '获取课程失败'
#
#         return Response(ret)


# 方式二
# View
# ApiView
# GenericViewSet
from rest_framework.viewsets import GenericViewSet,ViewSetMixin


class CourseView(ViewSetMixin, APIView):

    def list(self, request, *args, **kwargs):
        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000, 'data':None}
        try:
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000, 'data':None}
        try:
            # 课程ID=2
            pk = kwargs.get('pk')
            # 课程详细对象
            obj = models.CourseDetail.objects.filter(course_id=pk).first()
            ser = CourseDetailSerializer(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)


def test(request, *args, **kwargs):
    obj = models.Course.objects.filter(id=1).first()
    print(obj.name)
    print(obj.level)
    print(obj.get_level_display())
    return HttpResponse('...')


class MicroView(APIView):
    authentication_classes = [LuffyAuth,]

    def get(self, request, *args, **kwargs):
        ret = {'code':1000, 'data':'微职位'}

        return Response(ret)