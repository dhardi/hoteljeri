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

def index(request):
    rooms = Room.objects.all()
    print('rooms', rooms)
    return render(request, 'bookings/appbooking.html', {'rooms': rooms})

def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save_booking()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookings/appbooking.html', {'form': form})