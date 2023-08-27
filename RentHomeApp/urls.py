from django.urls import path
from . import views
from .views import renthomeapi

urlpatterns = [ 
    path("about/", views.about , name="About_us"),
    path("contact/", views.contact, name="contact_info"),
    path("register/", views.register, name="register"),  
    path("login/", views.login, name="login"),
    path("",views.index, name="index"),
    path("api/",renthomeapi.as_view(), name="homeapi"),
     ]