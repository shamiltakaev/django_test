from django.shortcuts import render
from .models import Author, Book
# Create your views here.
def main(request):
    return render(request, 'web_lib/main.html')

def authors(request):
    data = {"authors": Author.objects.all()}
    return render(request, "web_lib/authors.html", context=data)

def books(request):
    data = {"books": Book.objects.all()}
    return render(request, "web_lib/books.html", context=data)

def about(request):
    
    return render(request, "web_lib/about.html")