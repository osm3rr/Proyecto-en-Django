from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Personas

# Create your views here.

class HomePageView(ListView):
    template_name = "post.html"
    model = Post

class UsuariosView(ListView):
    template_name = "usuarios.html"
    model = Personas