
from rest_framework import serializers
from django.contrib.auth.models import User
from app_articles.models import Article
from accounts.models import UserProfile, UserAccess
from app_blog.models import BlogPost
from app_booking.models import Room, Booking
from app_mail.models import EmailANS, EmailDB 
from app_product.models import Product, ProductCategory
class ArticleSerializer( serializers.ModelSerializer):
  class Meta:
    model = Article
    fields=('__all__')
    # fields=('id','title','completed')
class BlogPostSerializer( serializers.ModelSerializer):
  class Meta:
    model = BlogPost
    fields=('__all__')

class BookingSerializer( serializers.ModelSerializer):
  class Meta:
    model =Booking
    fields=('__all__')    

class EmailDBSerializer( serializers.ModelSerializer):
  class Meta:
    model =EmailDB
    fields=('__all__')    

class EmailANSSerializer( serializers.ModelSerializer):
  class Meta:
    model =EmailANS
    fields=('__all__')    
class ProductCategorySerializer( serializers.ModelSerializer):
  class Meta:
    model =ProductCategory
    fields=('__all__')    

class ProductSerializer( serializers.ModelSerializer):
  class Meta:
    model = Product
    fields=('__all__')    



class RoomSerializer( serializers.ModelSerializer):
  class Meta:
    model =Room
    fields=('__all__')    

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=('__all__')


class UserProfileSerializer( serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields=('__all__')

class UserAccessSerializer( serializers.ModelSerializer):
  class Meta:
    model = UserAccess
    fields=('__all__')

