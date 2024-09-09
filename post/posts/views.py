from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class HomePageView(ListView): #Creando los posts en forma de lista (Más tarde se podrán editar)
    model = Post
    template_name = "home.html"