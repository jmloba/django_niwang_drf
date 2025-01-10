from django.contrib import admin
from django.urls import include, re_path,path

from accounts import views, urls


app_name ='accounts'

urlpatterns = [
  
  path('login-view/',views.login_view, name='login-view'),
  
  path('logout/',views.logout_view, name='logout-view'),  

  path('register/',views.register_view, name='register-view'), 

  path('forgot_password/',views.forgot_password, name='forgot-password'),  
  path('reset_Password_validate/<uidb64>/<token>/', views.reset_Password_validate, name ='reset_Password_validate'),  
  path('reset_password/',views.reset_Password, name='reset_Password'),       
]