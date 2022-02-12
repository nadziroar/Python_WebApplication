
from datetime import timezone
from xml.etree.ElementTree import tostring
from django.db import models

# Create your models here.

class StudentClass(models.Model):
    #Class for student classes
    className  = models.CharField(unique = True , max_length= 50)
    classMaxCapacity = models.IntegerField()
    classCurrentCapacity = models.IntegerField()
    createdDate = models.DateTimeField(auto_now_add= True)
    updateDate = models.DateTimeField(auto_now_add= True)
    
    
    #This is to return classname with current capacity
    def __str__(self):
        return self.className + ' Current Capacity : ' + str(self.classCurrentCapacity) + '/' + str(self.classMaxCapacity)
    
 
    
class Student (models.Model):
    #CLASS MODEL FOR STUDENT_INFORMATION
    studentID = models.IntegerField(primary_key= True)
    studentFirstName = models.CharField(max_length= 300)
    studentLastName = models.CharField (max_length= 300)
    studentClass = models.ForeignKey (StudentClass , on_delete= models.CASCADE)
    studentRegisterDate = models.DateTimeField (auto_now_add= True)
    studentEmail = models.CharField(unique = True , max_length= 300)
    studentStatus = ()