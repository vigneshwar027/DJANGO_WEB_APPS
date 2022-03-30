from django.db import models

# Create your models here.

class Document(models.Model):
    name = models.CharField(max_length=20, null=True,blank=True)
    file = models.FileField(upload_to='files',null=True,blank=True)
    photo = models.ImageField(upload_to='photos',null=True,blank=True)
    spec = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
