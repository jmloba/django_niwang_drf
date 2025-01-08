from django.urls import reverse
from app_booking.models import Room


def get_room_cat_url_list():
  '''
    function that returns the roomcategory and categoryurl list
  '''
  rooms = Room.objects.all()[0] # getting a random room object

  room_categories = dict(Room.ROOM_CATEGORIES) # mking a dictionary from "ROOM_CATEGORIES" tuple on the room
  room_cat_url_list=[]

  for category in room_categories:
    room_category = room_categories.get(category)
    room_url = reverse('app_booking:room-detail-view', kwargs={'category': category,})
    room_cat_url_list.append((room_category, room_url))
  return  room_cat_url_list 