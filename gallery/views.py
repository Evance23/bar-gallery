from django.shortcuts import render, redirect 
from django.http  import HttpResponse, Http404
from .models import Category, Photo
from gallery.forms import PostPhotoForm
# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos =Photo.objects.all()
    context = { 'categories': categories, 'photos': photos}
    return render(request, 'gallery/gallery.html', context)
  
def viewPhoto(request, photo_id):
    photo =Photo.objects.get(id=photo_id) 
    
    return render(request, 'gallery/photo.html', {'photo': photo})

  
  
def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST' :
        form = PostPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
        return redirect('/')
    else:
        form = PostPhotoForm()
    return render(request, 'gallery/add.html', {"form": form})

def search(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photo = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"photo": searched_photo})

    else:
        message ="The category you are searching for appears to be missing!"
        return render(request, 'gallery/search.html',{"message":message})

  