from django.conf.urls import url, include

from .views import CoursesListView,CoursesIndexView


app_name='[courses]'
urlpatterns=[
    url(r'^home/$',CoursesIndexView.as_view(),name="courses_home"),
    url(r'^list/$',CoursesListView.as_view(),name="courses_list")
]
