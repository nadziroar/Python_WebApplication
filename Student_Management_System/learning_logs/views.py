from django.shortcuts import render
from django.http import HttpResponse

from .models import StudentClass

def testing(request):
    return HttpResponse("Hello World im testing~")
# Create your views here.
def index(request):
    """The home page for learning_logs"""
    return render(request , 'learning_logs/index.html')

def student_class(request):
    """Show all student classes"""
    className = StudentClass.objects.order_by('className')
    context = {'classes' : className}
    return render(request, 'learning_logs/classes.html' , context)

