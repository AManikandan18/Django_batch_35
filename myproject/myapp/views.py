from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee,Student_Signals
# from myapp.models import Employee

from rest_framework import viewsets
from .models import Student_ser
from .serializer import StudentSerializer

# Create your views here.
def home(request):
    return HttpResponse('Welcome to Django...')

# Employee.objects.create(name = "Arul",age = 23)

# ORM :
# Queryset :

# data = Employee.objects.all() #Queryset
# print("Data :",data)
# for i in data:
#     print(i.name)

# Insert : 
# Employee.objects.create(name = 'nazar ali',age = 43)

#select * from Employee where age=23;
# data = Employee.objects.filter(age=23)
# print(data)

# Update:
# data = Employee.objects.get(id = 1)
# data.age = 25
# data.save()

# Delete :
# data = Employee.objects.get(id=4)
# data.delete()

#Joins Types:
# OneToOne
# OneToMany
# ManyToOne
# ManyToMany

# 2.Select Related:
# -----------------
    # select_related() performs a SQL JOIN and fetches related objects in one single query.

    # Use it when:
        # *You have ForeignKey
        # *You have OneToOneField
    
#without Select related:
# emp = Employee.objects.all() #select * from Employee
# for e in emp:
#     print(e.department.name) #Select name from department where id = 1;
                             #Select * from department where id = 2;
                             #Select * from department where id = 3;
                             #N+1 Queries.
                             
# Browser
#   ↓
# Employee Query  ───────────────► 1 query
#   ↓
# Loop starts
#   ├─ Department Query (IT) ────► 1 query
#   ├─ Department Query (IT) ────► 1 query
#   └─ Department Query (HR) ────► 1 query

# TOTAL = 1 + N queries (N = no. of employees)

# data = Employee.objects.select_related('department')
# for e in data:
#     print(e.department.name)

#Select Employee.*,Department.*
# From Employee
# inner join Department
# on Employee.department.id = department.id;
                             

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student_ser.objects.all()
    serializer_class = StudentSerializer

#Signals Value Inserted:
Student_Signals.objects.create(name = "Arul",age = 23)

Student_Signals.objects.create(name = "Jeeva",age = 24)
