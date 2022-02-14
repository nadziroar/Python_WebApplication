from django.shortcuts import render

from .models import StudentClass

# Create your views here.
def index(request):
    """The home page for learning_logs"""
    return render(request , 'learning_logs/index.html')

def student_class(request):
    """Show all student classes"""
    className = StudentClass.objects.order_by('createdDate')
    context = {'classes' : className}
    return render(request, 'learning_logs/className.html' , context)

