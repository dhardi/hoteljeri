from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Room model
class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(null=True, blank=True)
    image_url_main = models.URLField(blank=True)
    description = models.TextField(blank=True, default='')
    price_per_night = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    small_image_url_1 = models.URLField(blank=True)
    small_image_url_2 = models.URLField(blank=True)
    small_image_url_3 = models.URLField(blank=True)


# Booking model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    created_at = models.DateTimeField(default=timezone.now)

    def duration(self):
        return self.end_time - self.start_time


# Review model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} - {self.rating} stars'


