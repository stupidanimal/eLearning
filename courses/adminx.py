# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/4/20 14:51'

import xadmin

from .models import Course,CourseResourse,Lesson,Video

class CourseAdmin(object):
    list_display=['coursename','desc','detial','learn_times','students','click_nums','createdatetime']
    search_display = ['coursename', 'desc', 'detial',  'students', 'click_nums']
    list_filter=['coursename', 'desc', 'detial',  'students', 'click_nums']
    pass

class LessonAdmin(object):
    list_display = ['course', 'lessonname', 'createdatetime']
    search_display = ['course', 'lessonname', 'createdatetime']
    list_filter = ['course', 'lessonname', 'createdatetime']
    pass

class VideoAdmin(object):
    list_display = ['Lesson', 'videoname', 'createdatetime']
    search_display = ['Lesson', 'videoname', 'createdatetime']
    list_filter = ['Lesson', 'videoname', 'createdatetime']

class CourseResourseAdmin(object):
    list_display = ['Course', 'CourseResoursename', 'download','add_time']
    search_display = ['Course', 'CourseResoursename', 'download','add_time']
    list_filter = ['Course', 'CourseResoursename', 'download','add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResourse,CourseResourseAdmin)