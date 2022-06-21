from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from .models import  NeighbourHood, Profile, Post, Business
from django.contrib.auth.decorators import login_required
from.forms import NeighbourhoodForm, UpdateProfileForm,PostForm,BusinessForm

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

@login_required
def home(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.admin = request.user
            neighborhood.save()
            return redirect('hood')
    else:
        form = NeighbourhoodForm()
        neighborhoods = NeighbourHood.objects.all()
        neighborhoods = neighborhoods[::-1]
    return render(request, 'index.html', {'form': form, 'neighborhoods': neighborhoods})