from django.urls import path
from .views import HomePageView,UsuariosView

urlpatterns= [
    path("", HomePageView.as_view(), name = "post"),
    path("usuarios",UsuariosView.as_view(),name="usuarios") 

]

