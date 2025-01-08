
from rest_framework import serializers

from app_articles.models import Article

# data model serializer
class  ArticleSerializer( serializers.ModelSerializer):
  class Meta:
    model = Article
    # fields=('title','slug','body','date', 'thumb','author',)

    fields=('__all__')
    # fields=('product_id','name','cost', )
