

from django.contrib import admin
from app_blog.models import Post
from django.contrib.auth.models import Permission  , User

# Register your models here.
class Postdmin(admin.ModelAdmin):
  list_display=('author','title','description','created_at','updated_at')
  ordering=('author','updated_at')
  list_editable =('title','description',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()


admin.site.register(Post,Postdmin )
admin.site.register(Permission )  

