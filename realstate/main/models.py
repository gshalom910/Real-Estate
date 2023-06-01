from email.mime import image
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class PropertyType(models.Model):
    types=models.CharField(max_length=40,blank=True,null=True,default=None)

    def __str__(self):
        return self.types

class Home(models.Model):
    status_choice=[('Sale','sale'),('Rent','rent')]
    title=models.CharField(max_length=40)
    ptype=models.ForeignKey(PropertyType,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(max_length=40,choices=status_choice)
    area_sqms=models.FloatField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    price=models.CharField(max_length=150)
    rooms=models.CharField(max_length=10)
    bath=models.IntegerField()
    bed=models.IntegerField()
    images=models.ImageField()
    description=models.TextField(blank=True,null=True)
    address=models.CharField(max_length=30)
    subarea=models.CharField(max_length=25)
    geolocation=models.CharField(max_length=45)
    conditioning=models.BooleanField()
    pool=models.BooleanField()
    security=models.BooleanField()
    reception=models.BooleanField()
    garbage=models.BooleanField()
    conditioning=models.BooleanField()
    pets=models.BooleanField()
    green_area=models.BooleanField()
    gym=models.BooleanField()
    wifi=models.BooleanField()
    sauna=models.BooleanField()
    parking=models.BooleanField()
    cleaning=models.BooleanField()
    dstv=models.BooleanField()
    generator=models.BooleanField()

    def __str__(self):
        return self.title

class Gallery(models.Model):
    prop=models.ForeignKey(Home,on_delete=models.CASCADE)
    images=models.FileField()

  

    
