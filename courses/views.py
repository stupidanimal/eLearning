from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

class CoursesListView(View):
    def get(self,request):
        '''
        获取全部的课程信息
        :param request:
        :return:
        '''
        return render(request,'courses_list.html',{

        })
