from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#   return HttpResponse("Hello")

def gibran(request):
    return HttpResponse("Hello Gibran!")

def ahad(request):
    return HttpResponse("Ahad Hello!")

def greet(request,name):
    return HttpResponse(f"Hello, {name}")

#Rendering a complete template on Request
def index(request):
    return render(request, "hello/index.html")