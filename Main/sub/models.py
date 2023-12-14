from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=255)
    Price=models.CharField(max_length=255)
    Brand=models.CharField(max_length=255)
    image=models.CharField(max_length=3000)
# Create your models here.
