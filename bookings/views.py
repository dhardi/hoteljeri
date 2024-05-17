from django.shortcuts import render
from django.views import generic
from .models import Room, Booking
from rooms.models import Post
from django.shortcuts import redirect
from .forms import BookingForm


# Create your views here.

def booking_success(request):
    return render(request, 'bookings/booking_success.html')

class PostList(generic.ListView):
    model = Post
    template_name = "bookings/appbooking.html"
    context_object_name = 'posts'

from django.shortcuts import render, redirect
from django.views import generic
from .models import Room, Booking
from rooms.models import Post
from .forms import BookingForm

# Create your views here.

def booking_success(request):
    return render(request, 'bookings/booking_success.html')

class PostList(generic.ListView):
    model = Post
    template_name = "bookings/appbooking.html"
    context_object_name = 'posts'

def index(request):
    if request.method == "GET":
        rooms = Room.objects.all()
        form = BookingForm()
        return render(request, 'bookings/appbooking.html', {'rooms': rooms, 'form': form})
    elif request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            logged_in_user = request.user
            form.save_booking(logged_in_user)
            return redirect('booking_success')
        else:
            rooms = Room.objects.all()
            return render(request, 'bookings/appbooking.html', {'form': form, 'rooms': rooms})
    else:
        rooms = Room.objects.all()
        form = BookingForm()
        return render(request, 'bookings/appbooking.html', {'form': form, 'rooms': rooms})