from django.db import models

from django.contrib.auth.models import User


    
class Student(models.Model):

    student_num = models.CharField(max_length=255)
    roll = models.CharField(max_length=255)
    dept= models.CharField(max_length=255)
    address = models.TextField()
    image = models.ImageField(upload_to='images/')
    mark =models.IntegerField(default = 1)
    adder = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
    
        return self.student_num
   
