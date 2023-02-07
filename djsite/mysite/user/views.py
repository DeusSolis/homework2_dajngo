from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def login_view(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")


def registration_view(request: HttpRequest) -> HttpResponse:
    return render(request, "registration_form.html")