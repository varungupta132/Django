from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Receipe(models.Model): 
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null= True ,blank= True )
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="receipe")
    receipe_view_count=models.IntegerField(default=1)
class Department(models.Model):
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department
    
    class Meta:
        ordering = ['department']
        

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)
    
    def __str__(self):
        return self.student_id

        
class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=0) 
    student_address = models.TextField()
    
    def __str__(self):
        return self.student_name
    
    class Meta:
        ordering = ["student_name"]
        verbose_name = "student"
