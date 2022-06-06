from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    cost = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.title 

class Bin(models.Model):
    title = models.CharField(max_length=200, null=True)
    cost = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.title 
    