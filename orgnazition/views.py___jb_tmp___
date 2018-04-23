from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Teacher,CourseOrg
from django.views import generic




def index(request):
    teacher_list = Teacher.objects.all()[:5]
    output = ','.join(teacher.name for teacher in teacher_list)
    return HttpResponse(output)

def test(request):
    return render(request, 'orgnazition/test.html', None)


class TestView(generic.ListView):
    template_name = 'orgnazition/test.html'
    context_object_name = 'teachers'
    def get_queryset(self):
        return Teacher.objects.all()


class TeacherListView(generic.ListView):
    template_name = 'orgnazition/teacherList.html'
    context_object_name = 'teachers'
    def get_queryset(self):
        return Teacher.objects.all()

class CourseOrgListView(generic.ListView):
    template_name = 'orgnazition/CourseOrgList.Html'
    context_object_name = 'courseOrgList'
    def get_queryset(self):
        return CourseOrg.objects.all()
