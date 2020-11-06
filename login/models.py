# _*_ coding:utf8 _*_
from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.AutoField(verbose_name="userId", primary_key=True)
    userName = models.CharField(verbose_name="userName", max_length=50)
    userNickName = models.CharField(verbose_name="userNickName", max_length=50)
    userPassWord = models.CharField(verbose_name="userPassWord", max_length=50)
    userEmail = models.CharField(verbose_name="userEmail", max_length=50)
    userPhone = models.CharField(verbose_name="userPhone", max_length=50)
    isAdmin = models.SmallIntegerField(verbose_name="isAdmin")
    last_login = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        unique_together = ('userId', 'userName')


