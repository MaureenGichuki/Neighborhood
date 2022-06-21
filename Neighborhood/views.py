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

@login_required
def profile(request):
    current_user=request.user
    profile = Profile.objects.filter(id=current_user.id).first()
    if request.method == 'POST':
        profileform = UpdateProfileForm(request.POST,request.FILES,instance=profile)
        if  profileform.is_valid:
            profileform.save(commit=False)
            profileform.user=request.user
            profileform.save()
            return redirect('profile')
    else:
        form=UpdateProfileForm()
    return render(request,'profile/profile.html',{'form':form})