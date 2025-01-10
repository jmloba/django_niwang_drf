from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Room(models.Model):
  ROOM_CATEGORIES=(
    ('YAC','AC'),
    # ('NAC','NON-AC'),
    ('DEL','DELUXE'),
    # ('KIN','KING'),
    # ('QUE','QUEEN'),

  )
  number= models.IntegerField()
  category = models.CharField(max_length  = 3 , choices = ROOM_CATEGORIES)
  beds=models.IntegerField()
  capacity = models.IntegerField()
  def __str__(self):
    return f'Room: {self.number}, Category :{self.category}, Beds: {self.beds}, Capacity:{self.capacity} '
  
class Booking(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  room= models.ForeignKey(Room, on_delete=models.CASCADE)
  check_in = models.DateTimeField()
  check_out = models.DateTimeField()
  confirmation = models.BooleanField(default=False, null=True, blank=True)
  def __str__(self):
    return f'user :{self.user} booked room {self.room} from {self.check_in} to {self.check_out}'
  def get_room_category(self):
    room_categories = dict(self.room.ROOM_CATEGORIES)
    room_category =room_categories.get(self.room.category)
    return room_category
  
  def get_cancel_booking_url(self):
    return reverse('app_booking:CancelBookingView', args=[self.pk])




