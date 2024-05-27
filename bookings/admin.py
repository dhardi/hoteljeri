from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


admin.site.register(Room)
admin.site.register(Review)

admin.site.register(Booking)
list_display = ('user', 'room', 'end_time')
list_filter = ('status','created_on',)
prepopulated_fields = {'slug': ('title',)}
summernote_fields = ('content',) 