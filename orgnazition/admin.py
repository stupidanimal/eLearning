from django.contrib import admin

from .models import Teacher,CityDict,CourseOrg

admin.site.register(Teacher)
admin.site.register(CityDict)
admin.site.register(CourseOrg)