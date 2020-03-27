import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'student_performance_management.settings'
django.setup()

from core_app.models import *
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


def select():
    """查询操作"""
    try:
        s1 = ClassInfo.objects.get(pk=1).students.all()
        print(s1)
    except ObjectDoesNotExist:
        print('你还没添加数据')
        return

    c1 = StudentInfo.objects.get(pk=2).classNo.className
    print(c1)

    c2 = StudentInfo.objects.get(pk=1).courses.all()
    print(c2)

    s2 = CourseInfo.objects.get(pk=3).students.all()
    print(s2)

    c3 = ScoreInfo.objects.get(studentNo=2, courseNo=2).score
    print(c3)

    s3 = [i.studentNo for i in CourseInfo.objects.get(pk=3).score.filter(score__lt=60).all()]
    print(s3)


def add():
    """添加操作"""
    class1 = ClassInfo.objects.filter(classNo=4)
    if class1.exists():
        class1.delete()
    class1 = ClassInfo(classNo=4, className='国贸162', institute='管理与经济学院', grade=2016, classNum=32)
    class1.save()

    student1 = StudentInfo.objects.filter(studentNo=5)
    if student1.exists():
        student1.delete()
    student1 = StudentInfo.objects.create(studentNo=5, studentName='赵苏', sex='男',
                                          birthday=timezone.datetime(year=1998, month=5, day=13, tzinfo=timezone.utc), native='汉',
                                          classNo=class1)

    course1 = CourseInfo.objects.filter(courseNo=15)
    if course1.exists():
        course1.delete()
    course1 = CourseInfo.objects.create(courseNo=15, courseName='Web开发', creditHour=2, courseHour=32,
                                        priorCourse='Python程序设计')
    course1.students.add(student1)

    score1 = ScoreInfo.objects.filter(studentNo=student1, courseNo=course1)
    if score1.exists():
        score1.delete()
    score1 = ScoreInfo()
    score1.studentNo = student1
    score1.courseNo = course1
    score1.term = '2019年下'
    score1.score = 68
    score1.save()


if __name__ == '__main__':
    select()
    add()
