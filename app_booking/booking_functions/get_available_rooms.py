from app_booking.models import Room
from app_booking.booking_functions.availability import check_availability


def get_available_rooms( category,check_in, check_out):
  '''
  function that gets category and returns room list 
  '''

  room_list = Room.objects.filter(category=category)  


  available_rooms =[]
  # populate the list 
  for room in room_list:
    if check_availability(room, check_in, check_out ):
      available_rooms.append(room)
  # check the length of the list    
  if len(available_rooms)> 0  :
    return available_rooms
  else : 
    return None
  

