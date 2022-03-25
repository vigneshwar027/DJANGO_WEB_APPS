from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class Test(models.Model):
    exam = models.TextField(blank= True,null=True)
    english = models.IntegerField(blank= True,null=True, unique=True)
    maths = models.IntegerField(blank= True,null=True, unique=True)
    language = models.IntegerField(blank= True,null=True, unique=True)
    social = models.IntegerField(blank= True,null=True, unique=True)
    biology = models.IntegerField(blank= True,null=True, unique=True)
    rank = models.IntegerField(blank= True,null=True, unique=True)
    
class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.TextField(blank= True,null=True)
    image = models.ImageField(upload_to = 'media',blank= True,null=True)
    department = models.TextField(blank= True,null=True)
    roll_no = models.IntegerField(blank= True,null=True, unique=True)
    dob = models.TextField(blank= True,null=True)
    doj = models.TextField(blank= True,null=True)
    contact = models.TextField(blank= True,null=True)
    email = models.TextField(blank= True,null=True)
    exams = models.ManyToManyField(Test,blank= True,null=True)





