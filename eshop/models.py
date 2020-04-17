from django.db import models
from django.shortcuts import reverse
from django.conf import settings
# Create your models here.

class Brands(models.Model):
   Brand_Name = models.CharField(max_length=100)
  #def __str__(self):
	#return (self,BrandName)
	
class Categories(models.Model):
   Category_Name = models.CharField(max_length=100)

#def __str__(self):
	#return (self,Category_Name)
	
class item(models.Model):

    Name = models.CharField(max_length=80)
    Image = models.ImageField(upload_to='pics')
    Price = models.FloatField()
    Discount = models.FloatField(blank=True, null=True)
    Slug = models.SlugField(max_length=80)
    Brand_Name = models.CharField(max_length=80)#
    Category_Name = models.CharField(max_length=80)#
    Colour = models.CharField(max_length=80)
    Size = models.CharField(max_length=80)
    Weight = models.FloatField()
    Discription = models.TextField(max_length=80)
    Modify_date = models.DateTimeField()
    Expiry_date = models.DateTimeField()
    Create_date = models.DateTimeField(auto_now_add=True)

def get_absulate_url(self):
	
   return reverse("shop:items",kwargs={
      'slug':self.Slug
   })
	


class Registration(models.Model):

    Logo = models.ImageField(upload_to='pics')
    Sitemoto = models.TextField(max_length=100)
    Phonenumber = models.TextField(max_length=31)
    Email = models.EmailField()
    Address = models.TextField(max_length=150)
    Facebook = models.URLField()
    Twitter = models.URLField()
    Googlepls = models.URLField()
    linkedin = models.URLField()
#def __str__(self):
	#return (self,Logo)
	
class User(models.Model):
   FirstName = models.CharField(max_length=100)
   LastName = models.CharField(max_length=100)
   UserName = models.CharField(max_length=100)
   Email = models.EmailField()
   Phonenumber = models.TextField()
   Password = models.CharField(max_length=50)
   RePassword = models.CharField(max_length=50)
#def __str__(self):
	#return (self,FirstName)
	
