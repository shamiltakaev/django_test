from django.urls import path
from .views import main, authors, books, about

urlpatterns = [
    path("", main, name="web_lib"),
    path("authors/", authors),
    path("books/", books),
    path("about/", about, name="about")
]