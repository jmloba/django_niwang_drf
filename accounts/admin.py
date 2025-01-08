from django.contrib import admin
from .models import UserProfile, UserAccess
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
  list_display=('user','avatar','cover_photo','bio')
  ordering=('user',)
  list_editable =('avatar','cover_photo',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()
class UserAccessAdmin(admin.ModelAdmin):
  list_display=('user','new_user','supervisor','post_task','Programmers')
  ordering=('user',)
  list_editable =('supervisor','new_user','post_task','Programmers')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  
admin.site.register(UserAccess, UserAccessAdmin)
admin.site.register(UserProfile, UserProfileAdmin)