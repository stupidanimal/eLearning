from django.db import models
from datetime import datetime

# Create your models here.
class Course(models.Model):
    '''
    课程信息
    '''
    level_choices=(
        (1,"初级"),
        (2,"中级"),
        (3,"高级")
    )
    cid=models.AutoField(primary_key=True)
    coursename=models.CharField("课程名",max_length=50)
    desc=models.CharField("描述信息",max_length=200)
    detial=models.TextField("课程详情",choices=level_choices,max_length=2)
    learn_times=models.IntegerField("学习时长",default=0)
    students=models.IntegerField("收藏人数",default=0)
    image=models.ImageField("封面图",upload_to="courses/%Y/%m",max_length=100)
    click_nums=models.IntegerField("点击数",default=0)
    createdatetime=models.DateTimeField("创建时间",default=datetime.now)

    class Meta:
        verbose_name="课程"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.coursename

class Lesson(models.Model):
    '''
    章节信息表
    '''
    course=models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    lessonname=models.CharField("章节名",max_length=100)
    createdatetime=models.DateTimeField("创建时间",default=datetime.now)

    class Meta:
        verbose_name="章节"
        verbose_name_plural=verbose_name

    def __str__(self):
        return '《{0}》课程的章节：{1}'.format(self.course,self.name)

class Video(models.Model):
    '''
    视频信息
    '''
    Lesson=models.ForeignKey(Lesson,verbose_name="章节",on_delete=models.CASCADE)
    videoname=models.CharField("视频名称",max_length=100)
    createdatetime=models.DateTimeField("创建时间",default=datetime.now)

    class Meta:
        verbose_name="视频"
        verbose_name_plural=verbose_name

class CourseResourse(models.Model):
    '''
    课程资源
    '''
    Course=models.ForeignKey(Course,verbose_name="课程",on_delete=models.CASCADE)
    CourseResoursename=models.CharField("名称",max_length=100)
    download=models.FileField("资源文件",upload_to="course/resource/%Y/%m",max_length=100)
    add_time=models.DateTimeField("添加时间",default=datetime.now)
    class Meta:
        verbose_name="课程资源"
        verbose_name_plural=verbose_name