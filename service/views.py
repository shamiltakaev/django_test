from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect


from .models import Product

# Create your views here.
def index(request: HttpRequest):
    return render(request, "index.html")

def page(request: HttpRequest, page: int):
    return HttpResponse(f"Вы перешли на страницу {page}")

# def about(request: HttpRequest):
#     return HttpResponse("Hello")

def about(request: HttpRequest, pk: int):
    print(Product.objects.all())
    try:
        var = Product.objects.get(pk=pk)
    except ObjectDoesNotExist as exc:
        print(exc)
        return Http404("Not Found data")
    return HttpResponse(Product.objects.all())

def json_show(req):
    data = {
        "name": "Shamil", 
        "age": 23,
        "phone": "Galaxy A30s"
    }
    return JsonResponse(data)