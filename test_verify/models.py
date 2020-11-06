from django.db import models

# Create your models here.
class User_zjw(models.Model):
    username=models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    phone=models.CharField(max_length=32,default='')
    email=models.CharField(max_length=32,default='')

class teacherquestion(models.Model):
    question=models.CharField(max_length=100,default='')
    detail = models.CharField(max_length=100,default='')
    author=models.CharField(max_length=32,default='')
    teacherbh=models.ForeignKey(User_zjw,on_delete=models.CASCADE,default='')