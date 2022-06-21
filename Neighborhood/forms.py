from django import forms
from .models import NeighbourHood,Profile,Post,Business

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']