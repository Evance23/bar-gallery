from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, null= False)
    
    def __str__(self):
        return self.name
    
    
class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True)
    image = CloudinaryField('image')
    description = models.TextField()
    
    def __str__(self):
        return self.description 

    @classmethod
    def get_photo_by_id(cls,id):
        photo = cls.objects.get(id=id)
        return photo

    @classmethod
    def search_by_category(cls,search_term):
        mypics = cls.objects.filter(category__name__icontains=search_term)
        return mypics