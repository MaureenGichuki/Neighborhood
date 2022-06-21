from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from .models import NeighbourHood,Profile,Post,Business

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','image')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'email','description','image')

class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')  