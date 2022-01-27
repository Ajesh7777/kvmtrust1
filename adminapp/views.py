from django.shortcuts import render
from django.urls import reverse #used for calling views in useraapp


# Create your views here.
def home(request):
    return render(request,'adminapp/home.html')

def photogallery(request):
    return render(request,'adminapp/photogallery.html')