from django.contrib import admin

from service.models import Bin, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Bin)