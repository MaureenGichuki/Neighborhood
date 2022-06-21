from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from .models import  NeighbourHood, Profile, Post, Business
from django.contrib.auth.decorators import login_required
from.forms import NeighbourhoodForm, UpdateProfileForm,PostForm,BusinessForm

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')