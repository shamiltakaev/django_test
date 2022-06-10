from django.urls import path
from .views import main, authors, books, about, author_id

urlpatterns = [
    path("", main, name="main"),
    path("authors/", authors, name="authors"),
    path("author/<int:pk>", author_id, name="author_id"),
    path("books/", books, name="books"),
    path("about/", about, name="about")
]