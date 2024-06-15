from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .models import Room, Booking

class RoomBookingViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.url = reverse('bookings')

    def test_booking_page_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="container mt-5">')
        self.assertContains(response, '<div class="alert alert-warning" role="alert">')
        self.assertContains(response, 'Please <a href="')
        self.assertContains(response, '">sign in</a> to book a room.')
        self.assertContains(response, '</div>')
        self.assertContains(response, '</div>')

    def test_booking_page_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Please <a href=\"/login/\">sign in</a> to book a room.")
        self.assertContains(response, '<h1>Book a Room</h1>')

    def test_booking_page_with_form_errors(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.url, {'room': '', 'start_time': '', 'end_time': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Oops! There was an error.')

class BookingTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser2', password='12345')
        self.client.login(username='testuser2', password='12345')
        self.room = Room.objects.create(name='Room 101')

    def test_update_booking(self):
        booking = Booking.objects.create(user=self.user, room=self.room, start_time=datetime.now(), end_time=datetime.now() + timedelta(hours=1))
        new_end_time = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        response = self.client.post(reverse('change_booking', kwargs={'pk': booking.pk}), {
            'room': self.room.pk,
            'start_time': booking.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'end_time': new_end_time
        })

        self.assertEqual(response.status_code, 302)  # Redirecionamento após atualização bem-sucedida

        updated_booking = Booking.objects.get(pk=booking.pk)
        self.assertEqual(updated_booking.end_time.strftime('%Y-%m-%d %H:%M:%S'), new_end_time)

    def test_delete_booking(self):
        booking = Booking.objects.create(user=self.user, room=self.room, start_time=datetime.now(), end_time=datetime.now() + timedelta(hours=1))
        response = self.client.post(reverse('delete_booking', kwargs={'pk': booking.pk}))
        self.assertEqual(response.status_code, 302)  # Redirecionamento após exclusão bem-sucedida

        # Verifica se o Booking foi excluído do banco de dados
        booking_exists = Booking.objects.filter(pk=booking.pk).exists()
        self.assertFalse(booking_exists, f"Booking with pk={booking.pk} still exists in the database.")
