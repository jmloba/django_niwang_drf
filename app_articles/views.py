from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.models import UserAccess

from app_articles.models import Article
from app_articles.forms import ArticleForm, CreateArticleForm
from app_articles.serializer import ArticleSerializer

from rest_framework import generics
from rest_framework import mixins

from rest_framework.views import APIView
from rest_framework import status

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


# permission_required='app_articles.add_article'

# create
@login_required(login_url='accounts:login_view')
def article_create(request):
  # accessing OneToOnefield
  # access rights
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
  
#--- for dashboard using mixins


class ListArticlesMixins(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    permission_classes=([IsAuthenticated])
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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

