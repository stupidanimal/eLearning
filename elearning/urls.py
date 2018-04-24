"""elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin

from django.urls import path,include
# url,include与上面的path不在一个模块下
from django.conf.urls import url,include
import xadmin
from rest_framework.documentation import include_docs_urls
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
# from xadmin.plugins import xversion
# xversion.register_models()

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    path('docs',include_docs_urls(title='my-dfr')),
    path('api-auth/', include('rest_framework.urls')),
    url('^course/', include('courses.urls', namespace="courses")),
    path('orgnazition/', include('orgnazition.urls')),
]
