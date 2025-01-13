from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

from rest_framework import generics, mixins, status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.views.generic.list import ListView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication 
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from rest_framework.response import Response

from app_articles.models import Article
from api.serializers import ArticleSerializer,ProductSerializer, UserSerializer
from app_product.models import Product




# Create your views here.
@api_view(['GET','POST'])
@authentication_classes((TokenAuthentication,))
def api_ProductList(request):
  query = Product.objects.all()
  serializer_class = ProductSerializer(query, many=True)
  print(f'*** serialized product: {serializer_class.data}')
  return Response(serializer_class.data)

class DetailArticleMixin(mixins.RetrieveModelMixin, 
                          mixins.UpdateModelMixin,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin, 
                          generics.GenericAPIView):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer

  def get(self, request,  *args, **kwargs):
    return self.retrieve(request, *args,**kwargs)
  
  def put(self, request,  *args, **kwargs):
    return self.update(request, *args,**kwargs)

  def post(self, request,  *args, **kwargs):
    return self.create(request, *args,**kwargs)
  

  def delete(self, request,  *args, **kwargs):
    return self.destroy(request, *args,**kwargs)   
  

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




class generic_UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]



class generic_ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
  
class ListProductsMixins(mixins.ListModelMixin, generics.GenericAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def get(self, request,*args, **kwargs):
    return self.list(request, *args,**kwargs)  
  

  #---------- django generic crud-----------------

class ListProductsGenerics(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class DetailProductGenerics(generics.RetrieveAPIView,
                            generics.UpdateAPIView,
                            generics.DestroyAPIView):
  
  queryset = Product.objects.all()
  serializer_class = ProductSerializer    


class DetailCreateProductGenerics(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer    

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset= Product.objects.all()
  serializer_class= ProductSerializer

  def get_permissions(self):
    self.permission_classes=[AllowAny]

    if self.request.method =='POST':
      self.permission_classes=[IsAdminUser]
    return super().get_permissions()  


class PremiumProducts(PermissionRequiredMixin, ListView):  
  template_name ="app_product/listpremiumProducts.html"
  model = Product
  context_object_name='product'
  # note  if using PermissionRequireMixin
  permission_required='app_product.view_product'
  paginate_by =2


 
class DetailProductMixins(mixins.RetrieveModelMixin, 
                          mixins.UpdateModelMixin,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin, 
                          generics.GenericAPIView):

  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def get(self, request,  *args, **kwargs):
    return self.retrieve(request, *args,**kwargs)
  
  def put(self, request,  *args, **kwargs):
    return self.update(request, *args,**kwargs)

  def post(self, request,  *args, **kwargs):
    return self.create(request, *args,**kwargs)
  

  def delete(self, request,  *args, **kwargs):
    return self.destroy(request, *args,**kwargs)
  