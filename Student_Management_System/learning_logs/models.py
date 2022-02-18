
from datetime import timezone
from xml.etree.ElementTree import tostring
from django.db import models
from django.forms import ModelForm

# Create your models here.

class StudentClass(models.Model):
    #Class for student classes
    name  = models.CharField(default= 'Empty Name',  max_length= 50)
    classMaxCapacity = models.IntegerField()
    classCurrentCapacity = models.IntegerField()
  
    
    #This is to return classname with current capacity
    def __str__(self):
        return self.name
    
 
class StudentClassForm (ModelForm):
    class Meta:
        model = StudentClass
        fields = ['name' , 'title' , 'createddate']
    