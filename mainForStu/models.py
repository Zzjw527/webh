# _*_ coding:utf8 _*_
from django.db import models

# Create your models here.

class ProblemsContent(models.Model):
    problemId = models.AutoField(verbose_name="problemId", primary_key=True)
    problemTitle = models.CharField(verbose_name="problemTitle", max_length=200)
    memoryLimit = models.IntegerField(verbose_name="details")
    timeLimit = models.IntegerField(verbose_name="input")
    problemDescription = models.TextField(verbose_name="problemDescription", max_length=500)
    inputDescription = models.TextField(verbose_name="inputDescription", max_length=500)
    outputDescription = models.TextField(verbose_name="outputDescription", max_length=500)
    # author = models.CharField(verbose_name="author", max_length=50)

class SubmitStatus(models.Model):
    submitTime = models.DateTimeField(verbose_name="submitTime")
    userName = models.CharField(verbose_name="userName", max_length=50)
    problemId = models.CharField(verbose_name="problemId", max_length=50)
    judgeResult = models.CharField(verbose_name="judgeResult", max_length=500)
    usedMemory = models.CharField(verbose_name="usedMemory", max_length=100)
    usedTime = models.IntegerField(verbose_name="usedTime")
    language = models.CharField(verbose_name="language", max_length=50)
    code = models.TextField(verbose_name="code", max_length=500)

class ProblemTestData(models.Model):
    problemId = models.CharField(verbose_name="problemId", max_length=50)
    number = models.IntegerField(verbose_name="number")
    inputData = models.TextField(verbose_name="inputData", max_length=500)
    outputData = models.TextField(verbose_name="outputData", max_length=500)
    isExample = models.SmallIntegerField(verbose_name="isExample")
    explanation = models.TextField(verbose_name="explanation", max_length=500)