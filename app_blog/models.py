from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE )
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __string__(self):
    return self.title+'\n'+self.description



