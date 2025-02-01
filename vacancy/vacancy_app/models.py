from django.db import models

# Create your models here.

class Vacancy(models.Model):
    name = models.CharField(max_length = 150)
    salary = models.IntegerField()
    description = models.TextField()
    company = models.ForeignKey('Company', on_delete = models.CASCADE)
    categories = models.ManyToManyField('Category')
    

class Company(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to = "images/")
    

class Category(models.Model):
    name = models.CharField(max_length = 150)
    