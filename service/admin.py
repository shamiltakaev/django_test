from django.contrib import admin

from service.models import Bin, Product, Home

# Register your models here.
admin.site.register(Bin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "id", "cost", "is_active"]

    fields = ["id", "title", "is_active"]
    list_filter = ["id", "cost"]
    search_fields = ["title", "id"]

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ["size", "cost", "addr", "bal"]