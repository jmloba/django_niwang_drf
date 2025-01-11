from django.shortcuts import redirect, render, HttpResponse
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
from app_product.mydecorator import custom_permission_required
from rest_framework import permissions
import requests
from app_product.mydecorator import custom_permission_required, group_required
from django.views.generic.list import ListView
from .mixins import CheckPremiumGroupMixin

#----------
# checking permission for function  based views
#----------

@custom_permission_required('app_product.view_product')
# @custom_permission_required('app_product.add_product')
def premiumProducts(request):
  print ('test default')
  # ct = ContentType.objects.get_for_model(Product)
  # if request.user.groups.filter(name='default').exists():
  # if request.user.permission.filter(codename='view_product', contenttype=ct).exists():

  data = Product.objects.all()
  product=ProductSerializer(data, many=True)
  print (f'premium product test {product.data} ')
  context={'product':product.data,}
  return render(request, 'app_product/listpremiumProducts.html', context)
  # else:
  #   return HttpResponse('no permission found in user')
  
#----------
# checking permission for class based views
#----------
from django.contrib.auth.mixins import PermissionRequiredMixin
# class PremiumProducts(CheckPremiumGroupMixin, ListView):
class PremiumProducts(PermissionRequiredMixin, ListView):  
  template_name ="app_product/listpremiumProducts.html"
  model = Product
  context_object_name='product'
  # note  if using PermissionRequireMixin
  permission_required='app_product.view_product'
  paginate_by =2


@login_required(login_url='accounts:login-view')
@api_view(['GET',])
def listproducts(request):
  query = Product.objects.all()
  serializer_class = ProductSerializer(query, many=True)
  form = ProductForm()
  # print(f'serialized product: {serializer_class.data}')
  context = {"data":serializer_class.data, 'form': form}
  template = 'app_product/dashboard_product.html'
  # return Response(serializer_class.data)
  return render(request,template,context)

@custom_permission_required('app_product.add_product')
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
  authentication_classes=[SessionAuthentication, BasicAuthentication ]
  

  def get(self,request,pk=None):
    data = Product.objects.get(pk=pk)
    form = ProductForm(instance=data)
    serializer_class = ProductSerializer(data, many=False)
    # return Response (serializer_class.data)    
    template ='app_product/product-update.html'
    context = {"data":serializer_class.data, 'form': form}
    return render(request,template,context)
  
  
  def post(self,request,pk=None):
    print(f' method is put  pk is :{pk}')
    data= request.data
    data_obj = Product.objects.get(pk=pk)
    serializer_obj=ProductSerializer(data_obj,data= data )

    if serializer_obj.is_valid(raise_exception=True):
      print(f' serializer is valid ')      
      product_saved= serializer_obj.save()
      response= {"success": "product : '{}' created successfully ".format(product_saved.name)}
      # return Response(response)
      return redirect('app_product:apiclass-ProductView', )




class apiclass_ProductDeleteView(APIView):
  def get(self,request,pk=None):
    print(f' method delete pk: :{pk}')
    data = Product.objects.get(pk=pk).delete()

    # return Response( status=status.HTTP_200_OK)
    return redirect('app_product:apiclass-ProductView', )
  

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





