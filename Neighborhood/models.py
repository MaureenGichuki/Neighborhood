from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

# Location 

class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    # save location
    def save_location(self):
        self.save()

    def __str__(self):
        return self.name

# Neighbourhood Model

class NeighbourHood(models.Model):

    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    occupants_count = models.IntegerField(default=0)
    police_count = models.IntegerField(default=0)
    hospital_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def create_neigborhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls, id):
        cls.objects.filter(id=id).delete()

    
    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    #Finding the neighbourhoods by id
    @classmethod
    def find_neigborhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood
    
    def __str__(self):
        return "%s neighborhood" % self.name

#Profile Model

class Profile(models.Model):
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to="profiles/")
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    joined =models.DateTimeField(auto_now=True)


    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    def __str__(self):
        return str(self.user)

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile 
              
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
   
# Post Model

class Post(models.Model):

    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    image =models.ImageField(upload_to = "pros/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.update()

# Business Model

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to ="photos/")

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()
    
    def __str__(self):
        return self.name
