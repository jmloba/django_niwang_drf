from django.contrib import admin
from django.urls import include, re_path,path
from app_members import views 

app_name ='app_members'


urlpatterns = [
  path('membersDashboard/',views.membersDashboard,name='membersDashboard'),

]