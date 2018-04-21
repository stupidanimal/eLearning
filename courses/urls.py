from django.conf.urls import url, include

from .views import CoursesListView


app_name='[courses]'
urlpatterns=[
    url(r'^list/$',CoursesListView.as_view(),name="courses_list")
]
