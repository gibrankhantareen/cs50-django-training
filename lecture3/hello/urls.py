from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("/gibran",views.gibran, name = "gibran"),
    path("/ahad",views.ahad, name="ahad"),
]