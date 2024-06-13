from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class RoomBookingViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.url = reverse('bookings')  # Ajuste este nome conforme necessário

    def test_booking_page_not_authenticated(self):
        response = self.client.get(self.url)
        print("Response content (not authenticated):", response.content.decode())  # Adicionado para debug
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
        print("Response content (authenticated):", response.content.decode())  # Adicionado para debug
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Please <a href=\"/login/\">sign in</a> to book a room.")
        self.assertContains(response, '<h1>Book a Room</h1>')

    def test_booking_page_with_form_errors(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.url, {'room': '', 'start_time': '', 'end_time': ''})
        print("Response content (form errors):", response.content.decode())  # Adicionado para debug
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Oops! There was an error.')