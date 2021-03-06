from django.urls import path, re_path

from service.views import index, page, about, json_show



urlpatterns = [
    path("", index, name="index"),
    re_path(r"service/(?P<page>\d{2})/$", page),
    path("about/<int:pk>", about, name="about"),
    path("json/", json_show, name="json_show")
]