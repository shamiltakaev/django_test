from django.shortcuts import render
from .models import Author, Book
from django.db.models import Count
# Create your views here.
def main(request):
    return render(request, 'web_lib/main.html')

def authors(request):
    data = {"authors": Author.objects.all()}
    return render(request, "web_lib/authors.html", context=data)

def author_id(request, pk):
    author = Author.objects.annotate(books_amount=Count("book")).get(pk=pk)
    # get(pk=pk)
    print(dir(author))
    # books_amount = author.annotate(books_amount=Count("book"))
    found_author = {"author": author}
    return render(request, "web_lib/author_id.html", found_author)

def books(request):
    data = {"books": Book.objects.all()}
    return render(request, "web_lib/books.html", context=data)

def about(request):
    return render(request, "web_lib/about.html")