from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hi, Brian!")

def david(request):
    return HttpResponse("Hi, David!")

def greetx(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
