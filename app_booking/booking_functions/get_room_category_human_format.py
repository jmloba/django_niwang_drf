
from django.urls import reverse
from app_booking.models import Room    
from django.shortcuts import render, redirect,HttpResponse

from app_booking.models import Room
    

def get_room_category_human_format(category):
  room = Room.objects.all()[0]
  room_category = dict(room.ROOM_CATEGORIES).get(category)
  return room_category
  
