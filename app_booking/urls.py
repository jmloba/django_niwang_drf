

from django.urls import include, re_path,path
from django.contrib import admin
from app_booking import views
from app_booking.views import RoomDetailView, RoomListView

app_name='app_booking'

urlpatterns = [
  re_path(r'^room_list_view/$',views.RoomListView, name='RoomList'),
  path('room_detail_view/<category>', RoomDetailView.as_view(), name='room-detail-view' ),

  # path('booking_list/', BookingList.as_view(), name ='BookingList'),  
]