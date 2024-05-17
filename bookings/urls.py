from . import views 
from django.urls import path

urlpatterns = [
    path('', views.index, name='bookings'),
    path('booking_success/', views.booking_success, name='booking_success'),
   # path('book_room/', views.book_room, name='book_room'),    
]