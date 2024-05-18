from django.shortcuts import render
from django.views import generic
from .models import Room, Booking
from rooms.models import Post
from django.shortcuts import redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


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


#show the bookings for user logged

@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/user_bookings.html', {'bookings': bookings})


@login_required
def change_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('user_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/change_booking.html', {'form': form})

@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == "POST":
        booking.delete()
        return redirect('user_bookings')
    return render(request, 'bookings/confirm_delete.html', {'booking': booking})

