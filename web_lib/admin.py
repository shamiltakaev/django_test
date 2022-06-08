from django.contrib import admin
from .models import Author, Book
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "email", "lit_type"]
    fields = ["name", "age", "email", "lit_type"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "amount_pages", "published"]
    