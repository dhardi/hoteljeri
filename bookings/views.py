from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Booking
from rooms.models import Post
from .forms import BookingForm, ReviewForm
from django.core.exceptions import ValidationError


# Class-based view to list posts
class PostList(generic.ListView):
    model = Post
    template_name = "bookings/appbooking.html"
    context_object_name = 'posts'


# View to handle booking index
def index(request):
    rooms = Room.objects.all()
    print("those are rooms = ", rooms)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save(user=request.user)
                messages.success(request, "Booking successful!")
                return redirect('booking_success')
            except ValidationError as e:
                messages.error(request, str(e))
    else:
        form = BookingForm()
    return render(request, 'bookings/appbooking.html',
                  {'rooms': rooms, 'form': form})


# View to show user bookings
@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/user_bookings.html',
                  {'bookings': bookings})


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
                form.save(user=request.user)  # Recalculate amount to pay
                messages.success(request, "Booking updated successfully!")
                return redirect('user_bookings')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = BookingForm(instance=booking)
    return render(
        request, 'bookings/change_booking.html', {'form': form, 'rooms': rooms}
    )


# View to delete a booking
@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking deleted successfully!")
        return redirect('user_bookings')
    return render(request, 'bookings/confirm_delete.html',
                  {'booking': booking})


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
    booking = Booking.objects.last()
    total_price = booking.total_price if booking else 0  # add new amout to pay
    review_form = ReviewForm()

    return render(
        request, 'bookings/booking_success.html',
        {'total_price': total_price, 'review_form': review_form}
    )


@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Thanks for the review!')
            return redirect('booking_success')
    else:
        form = ReviewForm()

    return render(
        request, 'bookings/booking_success.html',
        {'review_form': form}
    )