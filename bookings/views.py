from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Booking
from rooms.models import Post
from .forms import BookingForm
from django.shortcuts import render, redirect




# Class-based view to list posts
class PostList(generic.ListView):
    model = Post
    template_name = "bookings/appbooking.html"
    context_object_name = 'posts'

# View to handle booking index
def index(request):
    rooms = Room.objects.all()
    print("those are rooms = ",rooms)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save_booking(request.user)
                messages.success(request, "Booking successful!")
                return redirect('booking_success')
            except ValidationError as e:
                messages.error(request, str(e))
    else:
        form = BookingForm()
    return render(request, 'bookings/appbooking.html', {'rooms': rooms, 'form': form})

# View to show user bookings
@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/user_bookings.html', {'bookings': bookings})

# View to change a booking
@login_required
def change_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    rooms = Room.objects.all()
    print(rooms)  
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            try:
                form.save(user=request.user)  # O total_price será recalculado aqui
                messages.success(request, "Booking updated successfully!")
                return redirect('user_bookings')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/change_booking.html', {'form': form, 'rooms': rooms})

# View to delete a booking
@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking deleted successfully!")
        return redirect('user_bookings')
    return render(request, 'bookings/confirm_delete.html', {'booking': booking})

@login_required
def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(user=request.user)
            amount = str(booking.total_price)
            print("Amount to pay:", amount)
            return redirect('booking_success', amount=amount)  
    else:
        form = BookingForm()
    return render(request, 'bookings/book_room.html', {'form': form})

def booking_success(request):
    # Fetch the booking object from the database or calculate total price if not saved yet
    # Replace this with your actual logic to fetch the booking object
    booking = Booking.objects.last()  # Example: Fetch the last booking object
    total_price = booking.total_price  # Assuming the total price is saved in the booking object

    return render(request, 'bookings/booking_success.html', {'total_price': total_price})