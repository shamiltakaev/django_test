from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, null=True)
    cost = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(verbose_name="Активен", default=True)

    def __str__(self) -> str:
        return self.title 

class Bin(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, null=True)
    cost = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.title 
    

class Home(models.Model):
    id = models.IntegerField(primary_key=True)
    size = models.DecimalField(verbose_name="Размер", null = True, decimal_places=2, max_digits=10)
    cost = models.IntegerField(verbose_name="Цена", null=True)
    addr = models.CharField(verbose_name="Адрес", default="Грозный", max_length=200)
    bal = models.BooleanField(verbose_name="Балкон", default=True)

    def __str__(self) -> str:
        return self.addr