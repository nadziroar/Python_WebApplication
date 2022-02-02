"""Defines URL patterns for registration_apps"""

from django.urls import path

from . import views

app_name = 'registration_apps'
urlpatterns = [
    #Home Page : 
    path('' , views.index , name = 'index'),
    #Page that shows all students 
    path('students/' , views.students , name= 'students'),
    
]
