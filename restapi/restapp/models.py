from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=50)
    task_desc = models.TextField()
    task_img = models.ImageField(upload_to='task_img',null=True,blank=True)

    def image(self):
        try: 
            age = self.task_img.url
            
        except:
            age = ''
            
        return age

    
    
    def __str__(self):
        return '{}__{}'.format(self.task,self.task_desc)

    
