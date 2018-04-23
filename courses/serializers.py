# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/4/23 15:43'

from rest_framework import serializers
from .models import Course


# class CoursesSerializer(serializers.Serializer):
#     level_choices = (
#         ("1", "初级"),
#         ("2", "中级"),
#         ("3", "高级")
#     )
#     cid = serializers.AutoField()
#     coursename = serializers.CharField(required=True, max_length=50)
#     desc = serializers.CharField( max_length=200)
#     detial = serializers.TextField( choices=level_choices, max_length=2)
#     learn_times = serializers.IntegerField( default=0)
#     students = serializers.IntegerField( default=0)
#     image = serializers.ImageField()
#     click_nums = serializers.IntegerField(default=0)
#     createdatetime = serializers.DateTimeField()

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'