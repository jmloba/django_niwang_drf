
from django.contrib.auth.models import User


from rest_framework import serializers

from app_product.models import Product

# data model serializer
class  ProductSerializer( serializers.ModelSerializer):
  class Meta:
    model = Product
    # fields=('category_name','product_id','name','cost', 'date','description',)

    fields=('__all__')
    # fields=('product_id','name','cost', )

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=('__all__')



#simple serializer
class MessageSerializer(serializers.Serializer)   :

  email = serializers.EmailField()
  name = serializers.CharField(max_length=50)
  created = serializers.DateTimeField()
