from django.db import models

class Company(models.Model):
    company_id= models.AutoField(primary_key= True)
    name= models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about=models.TextField()
    Type= models.CharField(max_length=50,choices=
                           (
                               ('IT','IT'),
                               ('Non IT', 'Non IT'),
                               ('Mobail Phones','Mobail Phones')
                           ))
    added_date=models.DateField(auto_now=True)
    active= models.BooleanField(default=True)
    
    def __str__(self):
        return self.name+self.location
    
class Employee(models.Model):
    employee_id= models.AutoField(primary_key= True)
    name = models.CharField(max_length=50)
    email=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    phone = models.CharField( max_length=50)
    about= models.TextField()
    position=models.CharField(max_length=50,choices=(
        ('Manager','Manager'),
        ('Sortware Developer', 'sd'),
        ('project','pl')
        ))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)

    