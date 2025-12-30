from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
# class Department(models.Model):
#     name = models.CharField(max_length=50)
    
    
# class Employee(models.Model):
#     name = models.CharField(max_length=50)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)


# Serialization: 
#     Converts complex data, such as Django models or querysets, into JSON or XML format.

# Viewsets :
#     Define views that handle API requests and responses.

class Student_ser(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

#Signals:
class Student_Signals(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    