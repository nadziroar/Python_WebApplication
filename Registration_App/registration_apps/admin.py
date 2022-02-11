from django.contrib import admin

# Register your models here.
from .models import StudentClass , StudentInfo

admin.site.register(StudentClass)
admin.site.register(StudentInfo)
