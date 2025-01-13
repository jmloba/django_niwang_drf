from django.db import models

# Create your models here.
from django.utils.text import slugify

from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100 , unique=True)
  slug = models.SlugField(max_length=100, unique=True)
  body = models.TextField(max_length=2000)
  date = models.DateTimeField(auto_now_add=True)
  thumb= models.ImageField(default='default.jpg',null=True,blank=True,upload_to='images/')
  author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
  def save(self,*args,**kwargs):
    self.slug = slugify(self.title)
    super().save(*args,*kwargs)
  def __str__(self):
    return self.title
  def snippet(self):
    return self.body[:300]