from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.gallery,name = 'gallery'),
    url('photo/<int:photo_id>/', views.viewPhoto,name = 'photo'),
    url('add/',views.addPhoto,name = 'add'),
    url(r'^search/', views.search, name='search_results'),

]