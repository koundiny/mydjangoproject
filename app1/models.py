from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField(max_length=10)
    course = models.CharField(max_length=20)
    fee = models.PositiveIntegerField()
    address = models.CharField(max_length=100)