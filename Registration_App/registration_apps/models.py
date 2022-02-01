from django.db import models

# Create your models here.
class StudentClass (models.Model):
    #Class of class name,  how many maximum students capacity?
    name = models.CharField(max_length = 200)
    max_capicity = models.PositiveSmallIntegerField()
    current_capacity = 0 
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        #To display the class information
        class_info = f"Class Name : {self.name} \n Maximum Capacity : {self.max_capicity}"
        return class_info

class StudentInfo (models.Model):
    #Class of Student first name, last name, age , gender, email ,  class, status
    
    id = models.BigAutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    age = models.PositiveSmallIntegerField()
    gender = ('M' , 'Male') , ('F' , 'Female')
    student_class = models.ForeignKey(StudentClass ,on_delete=models.CASCADE)
    status = (1 , 'Registered') ,  (2 , 'Accepted') , ( 3 , 'Probation') , (4 , 'LOA') ,(5 , 'Graduated') , (6, 'Expelled')
    
    def __str__(self):
        #To display Student Info
        student_info = f"Student ID : {self.id} Student Name : {self.first_name}"
        return student_info