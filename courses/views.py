from django.db.models import Q

from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from django.core import serializers
from .models import Course
# Create your views here.

class CoursesIndexView(View):
    def get(self,request):
        '''
        获取全部的课程信息
        :param request:
        :return:
        '''
        # list_all_courses=Course.objects.all()
        return render(request,'courses_list.html',{
            # "allcourses":list_all_courses
        })

class CoursesListView(View):
    def get(self,request):
        '''
        获取全部的课程信息
        :param request:
        :return:
        '''
        # 1 获取全部的课程集合
        list_all_courses=Course.objects.all()
        # 2 序列化
        json_courses=serializers.serialize(list_all_courses)
        return JsonResponse({'allcourses':json_courses})
        # return render(request,'courses_list.html',{
        #     "allcourses":list_all_courses
        # })
