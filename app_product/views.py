from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from app_product.models import Product, ProductCategory
from app_product.forms import ProductForm
from app_product.serializer import ProductSerializer,MessageSerializer, UserSerializer, ProductCategorySerializer
from app_product.tests import Messageconvert 

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes

from rest_framework import viewsets
from rest_framework import routers

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.decorators import login_required



import requests



# function view

@authentication_classes([BasicAuthentication, SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@login_required(login_url='accounts:login-view')
@api_view(['GET',])
def listproducts(request):
  query = Product.objects.all()
  serializer_class = ProductSerializer(query, many=True)
  

  form = ProductForm()
  print(f'serialized product: {serializer_class.data}')

  context = {"data":serializer_class.data, 'form': form}
  template = 'app_product/dashboard_product.html'
  # return Response(serializer_class.data)
  return render(request,template,context)


@api_view(['POST',])
def product_addrecord(request):
  if request.method =='POST':
    form= ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('app_product:apiclass-ProductView', )
    

#---------- test purposes  -------------------

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def api_ProductList(request):
  query = Product.objects.all()
  serializer_class = ProductSerializer(query, many=True)
  print(f'*** serialized product: {serializer_class.data}')
  return Response(serializer_class.data)

#---------- function based views  -------------------


@api_view(['GET','POST'])
def ListMessages(request):

  message_obj = Messageconvert( email='RicaThoorn@emial.com',
  name =  'abj')

  print(f'message object : {message_obj}')

  serialize_class = MessageSerializer(message_obj,many=False)

  return Response(serialize_class.data)
#---------- class based views  -------------------

class apiclass_ProductView(APIView):
  authentication_classes=[SessionAuthentication, BasicAuthentication ]

  def get(self,request):
    data = Product.objects.all()
    form = ProductForm()
    serializer_class = ProductSerializer(data, many=True)
    print(f'**serialized Product: \n {serializer_class.data}')
    template = 'app_product/dashboard_product.html'
    context = {"data":serializer_class.data, 'form': form}
  
    # return Response (serializer_class.data)
    return render(request,template,context)
  
  ## add record
  def post(self, request, ):
    serializer_obj=ProductSerializer(data= request.data)
    if serializer_obj.is_valid(raise_exception=True):
      product_saved= serializer_obj.save()
      response= {"success": "product : '{}' created successfully ".format(product_saved.name)}
      # return Response(response)
      return redirect('app_product:apiclass-ProductView', )
    
    return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
  


class apiclass_ProductDetailView(APIView):
  def get(self,request,pk=None):
    data = Product.objects.get(pk=pk)
    form = ProductForm(instance=data)
    serializer_class = ProductSerializer(data, many=False)
    template ='app_product/product-detail.html'

    context = {"data":serializer_class.data, 'form': form}
    # return Response (serializer_class.data)    
    return render(request,template,context)
  
class apiclass_ProductUpdateView(APIView):
  def get(self,request,pk=None):
    data = Product.objects.get(pk=pk)
    form = ProductForm(instance=data)
    serializer_class = ProductSerializer(data, many=False)
    # return Response (serializer_class.data)    
    template ='app_product/product-update.html'
    context = {"data":serializer_class.data, 'form': form}
    return render(request,template,context)
  def put(self,request,pk=None):
    print(f' method is put  pk is :{pk}')
    data= request.data
    data_obj = Product.objects.get(pk=pk)
    serializer_obj=ProductSerializer(data_obj,data= data )

    if serializer_obj.is_valid(raise_exception=True):
      print(f' serializer is valid ')      
      product_saved= serializer_obj.save()
      response= {"success": "product : '{}' created successfully ".format(product_saved.name)}
      return Response(response)
      # return redirect('app_product:apiclass-ProductView', )
  
class apiclass_ProductDeleteView(APIView):
  def get(self,request,pk=None):
    print(f' method delete pk: :{pk}')
    data = Product.objects.get(pk=pk).delete()

    return Response( status=status.HTTP_200_OK)
    # return redirect('app_product:apiclass-ProductView', )
  

#---------- generic view  -------------------
class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset= Product.objects.all()
  serializer_class= ProductSerializer

  def get_permissions(self):
    self.permission_classes=[AllowAny]

    if self.request.method =='POST':
      self.permission_classes=[IsAdminUser]
    return super().get_permissions()  





class generic_UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


    
   
class ListProductsMixins(mixins.ListModelMixin, generics.GenericAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def get(self, request,*args, **kwargs):
    return self.list(request, *args,**kwargs)

   
class DetailProductMixins(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):

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

#---------- calling api via requests -----------------

class generic_ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

@api_view(['GET'])
def listproducts2(request):
  print(f'request : {request}')

  # # ###========
  # print(f'calling request')
  # # # after installing "requests"
  # print(f"\n calling-->> requests.get('http://127.0.0.1:8000/app_product/generic-ProductList/') ")


  # response = requests.get('http://127.0.0.1:8000/app_product/generic-ProductList/')

  # #  # transfor the response to json objects
  # data = response.json()
  # # print(f'\n\n ***** data  after getting response: {data}\n')
  # ###========
  data='test'
  return Response(data)
  
  # form = ProductForm()
  # context = {"data":response, 'form': form}
  # template = 'app_product/dashboard_product.html'
  # return render(request,template,context)
  


#---------- viewsets -----------------
# modelviewset has all the operation
# class ProductViewSet(viewsets.ModelViewSet):
#   queryset= Product.objects.all()
#   serializer_class = ProductSerializer

#---------- viewsets -----------------
# RO readonly

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
  queryset= Product.objects.all()
  serializer_class = ProductSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
  queryset= ProductCategory.objects.all()
  serializer_class = ProductCategorySerializer





