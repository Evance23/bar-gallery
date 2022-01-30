from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.gallery,name = 'gallery'),
    url('photo/<str:pk>/', views.viewPhoto,name = 'photo'),
    url('add/',views.addPhoto,name = 'add'),
]