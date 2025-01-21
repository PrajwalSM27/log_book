from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
  
    path("",views.home,name='home'),
    path("about",views.about,name='about'),
    path("home",views.home,name='home'),
    path("contact",views.home,name="home")
   
]
