from django.contrib import admin
from .models import Booking, Room

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
  list_display=('user','room','check_in','check_out')
  ordering=('room','check_in','check_out')
  list_editable =('room','check_in','check_out')
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class RoomAdmin  (admin.ModelAdmin):
  list_display=('number','category','beds','capacity')
  ordering=('number',)
  # list_editable =('room','check_in','check_out')
  filter_horizontal=()
  list_filter =()
  fieldsets=()



admin.site.register(Booking, BookingAdmin)

admin.site.register(Room, RoomAdmin)