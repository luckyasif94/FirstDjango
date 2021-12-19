from django.db import models

# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=20)

class Registration(models.Model):
    Fullname = models.CharField(max_length=100)
    Email = models.EmailField()
    Gender = models.CharField(max_length=30)
    mobile = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)

class UploadImage(models.Model):
    imagename = models.FileField(upload_to='img')
    login = models.IntegerField()