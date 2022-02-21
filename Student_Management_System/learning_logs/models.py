
from datetime import timezone
from xml.etree.ElementTree import tostring
from django.db import models
from django.forms import ModelForm

# Create your models here.

class ClassInfo(models.Model):
    #Class for student classes
    name  = models.CharField(default= 'Empty Name',  max_length= 50)
    classMaxCapacity = models.IntegerField()
    classCurrentCapacity = models.IntegerField()
  
    
    #This is to return classname with current capacity
    def __str__(self):
        return self.name
    
 
class Student (models.Model):
    #Class for Students
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date  = models.DateField()
    STATUS = [
        ('R' , 'Registered'),
        ('A' , 'Active'),
        ('P' , 'Probation'),
        ('E' , 'Expelled'),
        ('G' , 'Graduated'),
    ]
    GENDER = [
        ('m' , 'Male'),
        ('f' , 'Female'),
    ]
        