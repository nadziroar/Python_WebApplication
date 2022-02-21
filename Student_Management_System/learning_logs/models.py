
from datetime import timezone
from enum import unique
from msilib.schema import Class
from pydoc import classname
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
    classname = models.ForeignKey(ClassInfo, on_delete= models.CASCADE)
    id = models.AutoField(primary_key= True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification = models.IntegerField(unique= True)
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
    YEAR_IN_SCHOOL_CHOICES = [
        (1 , 'Year 1'), 
        (2 , 'Year 2'),
        (3 , 'Year 3'), 
        (4 , 'Year 4'), 
        (5 , 'Year 5'), 
        (6 , 'Year 6'),
    ]
        