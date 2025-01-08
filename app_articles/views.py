from django.shortcuts import render
from app_articles.models import Article
from app_articles.forms import ArticleForm
from app_articles.serializer import ArticleSerializer

from rest_framework.views import APIView
from rest_framework import status


class article_detail_view(APIView):

  def get(self,request,pk=None):
    data = Article.objects.get(pk=pk)
    
    serializer_class = ArticleSerializer(data, many=False)
    template ='app_articles/article_detail_view.html'

    context = {"data":serializer_class.data}
    # return Response (serializer_class.data)    
    return render(request,template,context)


class apiclass_ArticleView(APIView):

  def get(self,request):
    data = Article.objects.all()
    form = ArticleForm()

    serializer_class = ArticleSerializer(data, many=True)

    print(f'**serialized Product: \n {serializer_class.data}')

    template = 'app_articles/dashboard_article.html'
    context = {"data":serializer_class.data, 'form': form}
  
    # return Response (serializer_class.data)
    return render(request,template,context)
