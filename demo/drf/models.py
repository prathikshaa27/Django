from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rollno = models.IntegerField(max_length=100)