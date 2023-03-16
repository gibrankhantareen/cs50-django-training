from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def gibran(request):
    return HttpResponse("Hello Gibran!")

def ahad(request):
    return HttpResponse("Ahad Hello!")
