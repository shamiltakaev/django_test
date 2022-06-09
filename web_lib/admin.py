from django.contrib import admin
from .models import Author, Book, Product, Store, ExtUser
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "email", "lit_type"]
    fields = ["name", "age", "email", "lit_type"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "amount_pages", "published"]


@admin.register(ExtUser)
class ExtUserAdmin(admin.ModelAdmin):
    list_display = ["desc", "is_logged", "user"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["name"]
