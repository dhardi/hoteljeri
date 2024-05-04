from django.shortcuts import render
from django.views import generic
from rooms.models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post
    template_name = "bookings/appbooking.html"