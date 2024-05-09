from django.shortcuts import render
from django.views import generic
from .models import Room
from rooms.models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post
    template_name = "bookings/appbooking.html"

def index(request):
    rooms = Room.objects.all()
    return render(request, 'appbooking.html', {'rooms': rooms})