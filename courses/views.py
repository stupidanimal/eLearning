from django.db.models import Q

from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse,HttpResponse
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course
from .serializers import CoursesSerializer
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

# class CoursesListView(View):
class CoursesListView(APIView):
    def get(self,request):
        '''
        获取全部的课程信息
        :param request:
        :return:
        '''
        # 1 获取全部的课程集合
        list_all_courses=Course.objects.all()
        # 2 序列化
        # 方式1：传统方式
        # json_courses=serializers.serialize("json",list_all_courses)
        # return HttpResponse(json_courses,content_type='application/json')
        # return JsonResponse(json_courses)
        # return render(request,'courses_list.html',{
        #     "allcourses":list_all_courses
        # })

        # 方式2：使用drf
        serialzer_courses=CoursesSerializer(list_all_courses,many=True)
        return Response(serialzer_courses.data)
