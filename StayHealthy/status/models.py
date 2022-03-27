from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.

class Disease(models.Model):
    name = models.TextField(blank=True,null=True)
    medicine = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class Patient(models.Model):
    SEX = (
        ('Male','Male'),
        ('Female','Female'),
        ('Third_gender','Third_gender'),
    )

    BLOOD = (
        ('O+ve','O+ve'),
        ('O-ve','O-ve'),
        ('A-ve','A-ve'),
        ('A+ve','A+ve'),
        ('AB+ve','AB+ve'),
        ('AB-ve','AB-ve'),
        ('B-ve','B-ve'),
        ('B+ve','B+ve')
    )

    user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    name = models.TextField(blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    sex = models.TextField(blank=True,null=True,choices=SEX)
    blood = models.TextField(blank=True,null=True,choices=BLOOD)   

    def __str__(self) -> str:
        return self.name

class Treatment(models.Model):

    SEVERITY = (
                ('Critical','Critical'),
                ('Moderate','Moderate'),
                ('Low','Low')
    )

    DOSAGE = (
                (1,1),
                (2,2),
                (3,3),
    )

    patient = models.ForeignKey(Patient,blank=True,null=True,on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease,blank=True,null=True,on_delete=models.CASCADE)
    severity = models.TextField(blank=True,null=True, choices=SEVERITY)
    checkup_date = models.DateTimeField(blank=True,null=True)
    next_checkup_date = models.DateTimeField(blank=True,null=True)
    completion = models.BooleanField(default=False)    
    stock = models.IntegerField(blank=True,null=True)
    dosage_per_day = models.IntegerField(blank=True,null=True,choices=DOSAGE)

    def __str__(self) -> str:
        return '{}-{}'.format(str(self.patient),str(self.disease))


