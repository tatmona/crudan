from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='uploads',default='default.png')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    date_of_birth = models.DateField()

def __str__(self):
    return self.name