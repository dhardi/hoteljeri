from . import views 
from django.urls import path

urlpatterns = [
    path('', views.index, name='bookings'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.user_bookings, name='user_bookings'),
    path('my-bookings/change/<int:pk>/', views.change_booking, name='change_booking'),
    path('my-bookings/delete/<int:pk>/', views.delete_booking, name='delete_booking'),
   # path('book_room/', views.book_room, name='book_room'),    
]