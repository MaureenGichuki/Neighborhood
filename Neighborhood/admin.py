from django.contrib import admin
from .models import  NeighbourHood, Profile, Post, Business, Location


# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Location)
