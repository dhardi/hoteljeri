from django import forms
from django.core.exceptions import ValidationError
from .models import Room, Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'start_time', 'end_time']

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        print("Start Time:", start_time)
        print("End Time:", end_time)

        # Validate start_time and end_time
        if start_time and end_time:
            if start_time >= end_time:
                raise ValidationError("End time must be after start time.")

            # Check for overlapping bookings
            overlapping_bookings = Booking.objects.filter(
                room=room,
                start_time__lt=end_time,
                end_time__gt=start_time
            )
            print("Overlapping Bookings:", overlapping_bookings)
            if overlapping_bookings.exists():
                raise ValidationError("This room is already booked for the given time period.")

        return cleaned_data

    def save_booking(self, logged_in_user):
        booking = self.save(commit=False)
        booking.user = logged_in_user
        booking.save()
        return booking