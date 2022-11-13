import email
from operator import mod
from pydoc import describe
from pyexpat import model
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# creating data about teacher by creating teacher model
class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=15)
    address=models.TextField()
    class Meta:
        verbose_name_plural="1. Teachers"


#creating course model
class CourseCategory(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    #ther below lines of code is for modification
    class Meta:
        verbose_name_plural="2. Course Catergories"


# course model
class Course(models.Model):
    catergory=models.ForeignKey(CourseCategory, on_delete=models.CASCADE)# if we delete category it will delete course 
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    class Meta:
        verbose_name_plural="3. Courses"



#student model
class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=15)
    address=models.TextField()
    interested_catergoies=models.TextField()
    class Meta:
        verbose_name_plural="4. Students"