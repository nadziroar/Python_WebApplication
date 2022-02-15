from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home Page
    path('', views.index , name = 'index'),
    #Page that shows all classes 
    path('student_class/' , views.student_class , name = 'classes'),
]
