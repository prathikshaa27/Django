from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
