import requests

from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from app_product.models import Product, ProductCategory
from app_product.forms import ProductForm
from app_product.serializer import ProductSerializer,MessageSerializer, UserSerializer, ProductCategorySerializer
from app_product.tests import Messageconvert 
from app_product.config import get_base_http
from app_product.mydecorator import custom_permission_required, group_required

from rest_framework.views import APIView
from rest_framework import generics,mixins,status,viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication 

from .mixins import CheckPremiumGroupMixin

@api_view(['GET',])
@login_required(login_url='accounts:login-view')
@custom_permission_required('app_product.view_product')
def listproducts(request):
  query = Product.objects.all()
  serializer_class = ProductSerializer(query, many=True)
  form = ProductForm()
  context = {"data":serializer_class.data, 'form': form}
  template = 'app_product/dashboard_product.html'
  return render(request,template,context)

@custom_permission_required('app_product.add_product')
@api_view(['POST',])
def product_addrecord(request):
  if request.method =='POST':
    form= ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('app_product:apiclass-ProductView', )
    



def getProductList(request):
  base_endpoint = get_base_http() 
  rev = reverse('app_product:api-product-list')
  token_obj = Token.objects.get_or_create(user=request.user)
  token = 'Token '+ str(token_obj[0])
  print(f'token obj :{token_obj} , {token_obj[0]}')
  print(f'token  : {token}')
  #------
  url = base_endpoint + rev
  headers=  {
    "Content-type":"application/jason",
    "Authorization": token,
  }
  param=''

  # data = requests.get(url , param, headers=headers) 
  res = requests.get(url ,  headers=headers)
  data=res.json()

  print(f'responseis -->:{res.json()}')
  template = 'app_product/displayAPIresult.html'
  context = {'data':data}
  return render(request,template,context)
  # return None

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
  # authentication_classes = [TokenAuthentication]
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



    
   


  



#---------- calling api via requests -----------------


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
  queryset= Product.objects.all()
  serializer_class = ProductSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
  queryset= ProductCategory.objects.all()
  serializer_class = ProductCategorySerializer





