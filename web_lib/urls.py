from django.urls import path
from .views import main, authors, books

urlpatterns = [
    path("/", main, name="web_lib"),
    path("/authors", authors, name="web_lib"),
    path("/books", books, name="web_lib"),
]