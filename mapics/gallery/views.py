from django.shortcuts import render, redirect 
# from .models import Location,Category,Images
from django.http  import HttpResponse, Http404
from .models import Category, Photo
# import numpy as num 
# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos =Photo.objects.all()
    context = { 'categories': categories, 'photos': photos}
    return render(request, 'gallery/gallery.html', context)
  
def viewPhoto(request, pk):
    photo =Photo.objects.get(id=pk) 
    
    return render(request, 'gallery/photo.html', {'photo': photo})
  
  
def addPhoto(request):
    categories = Category.objects.all()
    
    
    if request.method == 'POST' :

        data = request.POST
        image = request.FILES.get("image")
        
        if data ['category'] != 'none' : 
            category=Category.object.get(id= data['category'])
        elif data ['category_new'] != '':
            category, created = Category.object.get_or_create(name=data['category_new'])
        else:
            category = None
        
        photo = Photo.object.create(
            category = category
            description = data ['description']
        )
        
        
    context = { 'categories': categories}
    return render(request, 'gallery/add.html', context)
  