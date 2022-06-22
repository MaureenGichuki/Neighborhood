from django.test import TestCase
from .models import *


# Create your tests here.

# Location Model Tests
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Greece')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business = Business(name='Pizzeria')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_method(self):
        self.business.create_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        self.business.create_business()
        self.business.delete()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)


class PostTestClass(TestCase):
    def setUp(self):
        self.post = Post(title='Hello')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_method(self):
        self.post.create_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        self.post.create_post()
        self.post.delete()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)
