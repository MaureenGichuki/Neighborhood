from django import forms
from .models import NeighbourHood,Profile,Post,Business

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)

