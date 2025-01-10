from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import EmailDB,EmailANS


# list of emails received
class EmailDBAdmin(admin.ModelAdmin):

  list_display=('id','user','email_from','created_date','replied_date','replied',
  'email_body',)
  list_editable =('replied',)
  ordering=('-created_date',)

  filter_horizontal=()
  list_filter =()
  fieldsets=()

# answered email  
class EmailANSAdmin(admin.ModelAdmin):

  list_display=('email_from','email_to','email_ref_id','email_body','created_date','package_amount',)
  
  ordering=('-created_date',)

  filter_horizontal=()
  list_filter =()
  fieldsets=()

admin.site.register(EmailDB,EmailDBAdmin )  
admin.site.register(EmailANS,EmailANSAdmin )  