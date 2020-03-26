from django.contrib import admin
from core_app.models import *

# Register your models here.
admin.site.register([ClassInfo, StudentInfo, CourseInfo, ScoreInfo])
