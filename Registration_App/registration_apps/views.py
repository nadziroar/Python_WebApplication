from django.shortcuts import render
from .models import StudentInfo

# Create your views here.
def index(request):
    """The Home Page for Registration Page"""
    return render(request, 'registration_apps/index.html')

def students_information(request):
    """Show all students"""
    students_info = StudentInfo.objects.order_by('id')
    context = {'students' : students_info}
    return render (request , 'registration_apps/students.html', context)