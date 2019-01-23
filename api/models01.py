# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/22
@Author: Zhang Yafei
"""
from django.db import models


class Course(models.Model):
    """
    课程表
    """
    title = models.CharField(max_length=32, verbose_name='课程名称')
    course_img = models.CharField(verbose_name='课程图片',max_length=64)
    level_choice = (
        (1, '初级'),
        (2, '中级'),
        (3, '高级'),
    )
    level = models.IntegerField(verbose_name='课程难易程度', default=1, choices=level_choice)

    def __str__(self):
        return self.title


class CourseDetail(models.Model):
    """
    课程详细
    """
    course = models.OneToOneField(to=Course, on_delete=models.CASCADE)
    slogon = models.CharField(verbose_name='口号', max_length=255)
    why = models.CharField(verbose_name='为什么要学', max_length=255)
    recommend_courses = models.ManyToManyField(verbose_name='推荐课程', to=Course, related_name='rc')

    def __str__(self):
        return '课程详细-'+self.course.title


class Chapters(models.Model):
    """
    课程章节
    """
    course = models.ForeignKey(to=Course, verbose_name='所属课程', on_delete=models.CASCADE)
    num = models.IntegerField(verbose_name='章节')
    name = models.CharField(max_length=32, verbose_name='章节名称')

    def __str__(self):
        return self.course.title + '-' + self.name


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)


class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
    # 可以加超时时间
