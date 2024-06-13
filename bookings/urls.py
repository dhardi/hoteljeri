from . import views 
from django.urls import path
from .views import book_room, booking_success, index

urlpatterns = [
    path('', index, name='index'),  # Definir apenas uma URL para a página inicial
    path('booking-success/', booking_success, name='booking_success'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('booking-success/<str:amount>/', booking_success, name='booking_success_amount'),  # Nome distinto para evitar conflito
    path('my-bookings/', views.user_bookings, name='user_bookings'),
    path('my-bookings/change/<int:pk>/', views.change_booking, name='change_booking'),
    path('my-bookings/delete/<int:pk>/', views.delete_booking, name='delete_booking'),
    path('book-room/', book_room, name='book_room'),
]
    
    
   # path('book_room/', views.book_room, name='book_room'),    
