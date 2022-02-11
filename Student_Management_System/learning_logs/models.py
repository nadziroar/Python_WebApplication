from enum import unique
from pydoc import classname
from django.db import models

# Create your models here.

class StudentClass(models.Model):
    #Class for student classes
    classID = models.Index(unique = True)
    className  = models.CharField(max_length= 50)
    classMaxCapacity = models.IntegerField
    classCurrentCapacity = models.IntegerField
    createdDate = models.DateTimeField(auto_now_add= True)
    updateDate = models.DateTimeField(auto_now_add= True)
    
    #This is to return classname with current capacity
    def __str__(self):
        return self.classID + "." +self.className + "Current Capacity: " + self.classCurrentCapacity