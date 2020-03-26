from django.db import models

# Create your models here.


class MyCharField(models.Field):
    """自定义char类型的字段类"""
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(MyCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        """限定数据库表生成的字段类型为char，长度为max_length指定的值"""
        return 'char(%s)' % self.max_length


class ClassInfo(models.Model):
    classNo = MyCharField(max_length=10, primary_key=True, verbose_name='班级编号')
    className = models.CharField(max_length=30, null=False, verbose_name='班级名称')
    institute = models.CharField(max_length=30, null=False, verbose_name='所属学院')
    grade = models.SmallIntegerField(null=False, verbose_name='年级')
    classNum = models.SmallIntegerField(null=False, verbose_name='班级人数')

    class Meta:
        db_table = 'ClassInfo'


class StudentInfo(models.Model):
    studentNo = MyCharField(max_length=10, primary_key=True, verbose_name='学号')
    studentName = models.CharField(max_length=30, null=False, verbose_name='姓名')
    sex = MyCharField(max_length=2, null=False, verbose_name='性别')
    birthday = models.DateTimeField(null=False, verbose_name='出生日期')
    native = models.CharField(max_length=30, null=False, verbose_name='民族')
    classNo = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, related_name='students', verbose_name='所属班级')

    class Meta:
        db_table = 'StudentInfo'


class CourseInfo(models.Model):
    courseNo = MyCharField(max_length=10, primary_key=True, verbose_name='课程号')
    courseName = models.CharField(max_length=30, null=False, verbose_name='课程名')
    creditHour = models.DecimalField(max_digits=2, decimal_places=1, null=False, verbose_name='课程名')
    courseHour = models.SmallIntegerField(null=False, verbose_name='课时数')
    priorCourse = models.CharField(max_length=30, null=False, verbose_name='先修课程')
    students = models.ManyToManyField(StudentInfo, related_name='courses', verbose_name='上课学生')

    class Meta:
        db_table = 'CourseInfo'


class ScoreInfo(models.Model):
    studentNo = models.ForeignKey(StudentInfo, related_name='score', on_delete=models.CASCADE, verbose_name='学号')
    courseNo = models.ForeignKey(CourseInfo, related_name='score', on_delete=models.CASCADE, verbose_name='课程号')
    term = MyCharField(max_length=10, null=False, verbose_name='开课学期')
    score = models.DecimalField(max_digits=4, decimal_places=1, null=False, verbose_name='成绩')

    class Meta:
        unique_together = ('studentNo', 'courseNo')
        db_table = 'ScoreInfo'
