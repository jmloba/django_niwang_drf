from django.urls import include, re_path,path
from django.contrib import admin
from . import views

app_name='app_mail'

urlpatterns = [

  re_path(r'^email_me/$',views.email_me, name='email_me'),
  re_path(r'^emailList/$',views.email_list, name='email_list'),
  re_path(r'^emailin_delete/$',views.emailin_delete, name='emailin-delete'),
## form 
  re_path(r'^email_list_view/$',views.email_list_view, name='email-list-view'),
  re_path(r'^emailin_reply/$',views.email_reply, name='email-reply'),
  re_path(r'^answered_email/$',views.answered_email, name='answered-email'),
  
  re_path(r'^answered-email-toggle/$',views.answered_email_toggle, name='answered-email-toggle'),

  
]