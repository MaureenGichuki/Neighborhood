from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from .models import  NeighbourHood, Profile, Post, Business
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from.forms import NeighbourhoodForm, UpdateProfileForm,PostForm,BusinessForm, SignupForm

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def signup(request):  
    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            email = form.cleaned_data['email']
            name = form.cleaned_data['your_name']
            recipient = Profile(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
    else:  
               form = SignupForm()  

    return render(request, 'registration/registration_form.html', {'form': form})  

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

@login_required
def neighborhood(request, neighborhood_id):
    neighborhood = NeighbourHood.objects.get(id=neighborhood_id)
    if request.method == 'POST':
        form_post = PostForm(request.POST, request.FILES)
        business_form = BusinessForm(request.POST, request.FILES)
        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.neighbourhood = neighborhood
            post.user = request.user
            post.save()
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.neighbourhood = neighborhood
            business.user = request.user
            business.save()
            return redirect('neighbourhood', neighborhood_id)
    else:
        current_user = request.user
        post_form = PostForm()
        business_form = BusinessForm()
        neighborhood = NeighbourHood.objects.get(id=neighborhood_id)
        business = Business.objects.filter(neighbourhood_id=neighborhood)
        users = Profile.objects.filter(neighbourhood=neighborhood)
        posts = Post.objects.filter(neighbourhood=neighborhood)
    return render(request, 'neighbourhood.html', {'post_form':post_form, 'business_form': business_form, 'users':users,'current_user':current_user, 'neighborhood':neighborhood,'business':business,'posts':posts})

@login_required
def join_hood(request, neighborhood_id):
    neighborhood = get_object_or_404(NeighbourHood, id=neighborhood_id)
    request.user.profile.neighbourhood = neighborhood
    request.user.profile.save()
    return redirect('neighbourhood', neighborhood_id = neighborhood.id)

@login_required
def leave_hood(request, neighborhood_id):
    neighborhood = get_object_or_404(NeighbourHood, id=neighborhood_id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')

@login_required
def search_results(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_hoods = NeighbourHood.search_by_name(search_term)
        print(searched_hoods)
        message = f"{search_term}"

        return render(request, 'search.html',{"hoods": searched_hoods})

