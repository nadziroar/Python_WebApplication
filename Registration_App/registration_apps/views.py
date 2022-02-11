from django.shortcuts import render
from .models import StudentInfo, StudentClass

# Create your views here.
def index(request):
    """The Home Page for Registration Page"""
    return render(request, 'registration_apps/index.html')

def students_class(request):
    """Show all classes """
    student_class = StudentClass.objects.order_by('current_capacity')

def students_info(request):
    """Show all students"""
    students_info = StudentInfo.objects.order_by('id')
    context = {'student_info' : students_info}
    return render (request , 'registration_apps/students.html', context)