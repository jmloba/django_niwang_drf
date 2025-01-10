from django.contrib import admin
from django.urls import include, re_path,path
from app_blog import views 

app_name ='app_blog'


urlpatterns = [
  path('postdDshboard/',views.postDashboard,name='postDashboard'),
  path('postCreateRecord/',views.CreatePost,name='postCreateRecord')

]