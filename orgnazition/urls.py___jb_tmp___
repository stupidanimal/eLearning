from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.TestView.as_view(), name='test'),
    path('teacherList',views.TeacherListView.as_view(),name='teacherList'),
    path('courseOrgList',views.CourseOrgListView.as_view(),name='courseOrglist')
]
