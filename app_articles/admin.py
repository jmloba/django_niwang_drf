

from django.contrib import admin
from app_articles.models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
  list_display=('title','slug','body','date','thumb','author')
  ordering=('date',)
  list_editable =('body','thumb','author',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

admin.site.register(Article, ArticleAdmin)