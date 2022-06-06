from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Product, Bin

# Create your views here.
def index(request: HttpRequest):
    return HttpResponse("Hello World")

def page(request: HttpRequest, page: int):
    return HttpResponse(f"Вы перешли на страницу {page}")

def about(request: HttpRequest, pk: int):
    
    try:
        var = Product.objects.get(pk=pk)
    except ObjectDoesNotExist as exc:
        print(exc)
        return Http404("Not Found data")
    return HttpResponse(Product.objects.all())