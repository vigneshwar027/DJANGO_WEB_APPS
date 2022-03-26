from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

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

    def __str__(self) -> str:
        return self.name

class Test(models.Model):
    student = models.ForeignKey(Student,null=True,blank=True,on_delete=models.CASCADE)
    exam = models.TextField(blank= True,null=True)
    english = models.IntegerField(blank= True,null=True)
    maths = models.IntegerField(blank= True,null=True)
    language = models.IntegerField(blank= True,null=True)
    social = models.IntegerField(blank= True,null=True)
    biology = models.IntegerField(blank= True,null=True)
    rank = models.IntegerField(blank=True,null=True)

    @property
    def total(self):
        tot = (self.english+self.maths+self.language+self.social+self.biology)
        return tot  

    @property
    def percentage(self):
        perc = (self.total/6)
        return perc  
    
    def __str__(self) -> str:
        return '{}-{}'.format(str(self.student),self.exam)




