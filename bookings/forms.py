from django import forms
from django.core.exceptions import ValidationError
from .models import Room, Booking, Review


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'start_time', 'end_time']

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time:
            if start_time >= end_time:
                raise ValidationError("End time must be after start time.")
            # Check if has bookings
            overlapping_bookings = Booking.objects.filter(
                room=room,
                start_time__lt=end_time,
                end_time__gt=start_time
            ).exclude(pk=self.instance.pk)  # Update the booking
            if overlapping_bookings.exists():
                raise ValidationError(
                    "This room is already booked for the given time period."
                )

        return cleaned_data

    def calculate_amount(self):
        cleaned_data = self.cleaned_data
        room = cleaned_data.get('room')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if room and start_time and end_time:
            duration = (end_time - start_time).days
            amount = duration * room.price_per_night
            return amount
        return 0

    def save(self, commit=True, user=None):
        booking = super().save(commit=False)
        if user:
            booking.user = user
        # Calculate the total price and save it
        booking.total_price = self.calculate_amount()
        if commit:
            booking.save()
        return booking


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }

  