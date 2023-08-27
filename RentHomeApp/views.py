from django.shortcuts import render
from django.http import HttpResponse
from .models import UsersData, Contract, Transactions, RentHome
import datetime
from .serializers import homeserilizer
from rest_framework import generics

class renthomeapi(generics.ListAPIView):
    queryset = RentHome.objects.all()
    serializer_class=homeserilizer


# # Create your views here.
def index(request):
    home = RentHome.objects.all()[:3]
    # Contract=Contract.objects.all()[0:3]
    return render(request, "index.html",{'home':home,})
    # return render(request, 'index.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

def login(request):
    return render(request,'login.html',{})

def register(request):
    return render(request,'register.html',{})
