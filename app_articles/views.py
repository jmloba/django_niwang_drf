import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import response
from django.urls import reverse

from app_articles.models import Article
from app_articles.forms import ArticleForm, CreateArticleForm
from api.serializers import ArticleSerializer
from app_articles.config import get_base_http

from accounts.models import UserAccess


from rest_framework import generics, mixins, status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# permission_required='app_articles.add_article'

# create
@login_required(login_url='accounts:login_view')
def article_create(request):
  u = UserAccess.objects.get(user=request.user)
  
  if u.article_create is None:
    return redirect('articles:main_page')

  if request.method=='POST':
    form = CreateArticleForm(request.POST, request.FILES)

    if form.is_valid():
      instance = form.save(commit = False)
      instance.author = request.user
      instance.save()
      return redirect('app_articles:dashboard_articles')
    else :
      messages.info(request, form.errors)
  else:  
    form = CreateArticleForm()
  context={'form': form }
  return render(request,'app_articles/article_create.html', context) 

# -----  for article detail
def articleDetailSlug(request,pk=None):
  print(f'articleDetailSlug : routine ')
  query = Article.objects.get(pk=pk)
  data =ArticleSerializer(query, many=False)
  context = {"data":data.data}  
  template = 'app_articles/article_detail_view.html'

  return render(request, template, context)

# get api  ++ sample
def articleDetail(request, pk=None):
  print(f'article to view {pk}')

  base_endpoint = get_base_http() 
  rev = reverse('app_articles:articledetailMixin')
  token_obj = Token.objects.get_or_create(user=request.user)
  token = 'Token '+ str(token_obj[0])
  url = base_endpoint + rev 
  print('url is :{url}')
  headers=  {
    "Content-type":"application/jason",
    "Authorization": token,

  }
  

  res = requests.get(url ,  headers=headers) 
  
  data=res.json()

  print(f'responseis -->:{res.json()}')
  template = 'app_product/displayAPIresult.html'
  context = {'data':data}
  return render(request,template,context)



# -----  for dashboard
class apiclassViewAllArticles(APIView):
  def get(self,request):
    data = Article.objects.all()
    form = ArticleForm()
    serializer_class = ArticleSerializer(data, many=True)
    print(f'**serialized Product: \n {serializer_class.data}')
    template = 'app_articles/dashboard_article.html'
    context = {"data":serializer_class.data, 'form': form}
    # return Response (serializer_class.data)
    return render(request,template,context)  


@login_required(login_url='accounts:login_view')
def article_list2(request):
  articles = Article.objects.all().order_by('date')
  context ={ 'articles':articles}
  return render(request,'app_articles/article_list2.html', context)


class apiclass_ArticleDeleteView(APIView):
  def get(self,request,pk=None):
    print(f' method delete pk: :{pk}')
    data = Article.objects.get(pk=pk).delete()

    # return Response( status=status.HTTP_200_OK)
    return redirect('app_articles:dashboard_articles' )

#-------for detail 

class apiclassArticleDetailView(APIView):
  # permission_required='app_articles.delete_article'  
  def get(self,request,pk=None):
    data = Article.objects.get(pk=pk)
    serializer_class = ArticleSerializer(data, many=False)
    template ='app_articles/article_detail_view.html'
    context = {"data":serializer_class.data}
    # return Response (serializer_class.data)    
    return render(request,template,context)

