from django.shortcuts import render, redirect 
# from .models import Location,Category,Images
from django.http  import HttpResponse, Http404
# import numpy as num 
# Create your views here.

def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')