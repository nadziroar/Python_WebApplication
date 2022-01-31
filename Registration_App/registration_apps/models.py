from django.db import models

# Create your models here.
class StudentClass (models.Model):
    #Class of class name,  how many maximum students capacity?
    name = models.CharField(max_length = 200)
    max_capicity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__ 
