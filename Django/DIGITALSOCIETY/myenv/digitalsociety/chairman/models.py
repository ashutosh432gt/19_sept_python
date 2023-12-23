from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password=models.CharField(max_length=20)
    role=models.CharField(max_length=10)
    is_active=models.BooleanField(default=True)
    is_verify=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)

class Chairman(models.Model):
    userid=models.models.ForeignKey(User,on_delete=models.CASCADE)   
    firstname=models.CharField(max_length=20) 
    lastname=models.CharField(max_length=20)
    contactno=models.CharField(max_length=20,null=True)
    houseno=models.CharField(max_length=8)