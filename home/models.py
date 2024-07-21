from django.db import models

# Create your models here.
class Student(models.Model):
    # id=models.AutoField()
        # CharField for storing small to moderate-sized strings
    name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    
    # IntegerField for storing integers
    age = models.IntegerField()
    
    # EmailField for storing email addresses
    email = models.EmailField()
    
    # TextField for storing large text data
    address= models.TextField(null=True,blank=True)
    
    # ImageField for storing im age files
    # image = models.ImageField()    
    # FileField for storing generic file uploads
    file = models.FileField()
    

    

    