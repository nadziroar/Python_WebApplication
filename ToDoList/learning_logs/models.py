from pydoc import text
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Category (models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Tasks(models.Model):
    """Create a task """
    category = models.ForeignKey(Category , on_delete= models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name_plural = 'Tasks'

    def __str__(self) :
        return f"{self.text[:50]}"
