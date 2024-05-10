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
    print('rooms', rooms)
    return render(request, 'bookings/appbooking.html', {'rooms': rooms})