from django.shortcuts import render, redirect 
# from .models import Location,Category,Images
from django.http  import HttpResponse, Http404
# import numpy as num 
# Create your views here.

def gallery(request):
    return render(request, 'gallery/gallery.html')
  
def viewPhoto(request, pk):
    return render(request, 'gallery/photo.html')
  
  
def addPhoto(request):
    return render(request, 'gallery/add.html')
  