from django import forms
from .models import Room, Booking

class BookingForm(forms.Form):
    room = forms.ModelChoiceField(queryset=Room.objects.all(), empty_label="Select a room")
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        # Validate start_time and end_time
        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("End time must be after start time.")

        return cleaned_data

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'start_time', 'end_time']  # Replace with your actual fields

    def save_booking(self, logged_in_user):
        room = self.cleaned_data['room']
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        booking = Booking.objects.create(room=room, start_time=start_time, end_time=end_time, user=logged_in_user)
        return booking