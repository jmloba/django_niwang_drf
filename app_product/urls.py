
from django.contrib import admin
from app_product import views
from django.urls import include, re_path,path
from app_product.views import apiclass_ProductView, apiclass_ProductDetailView, apiclass_ProductUpdateView,apiclass_ProductDeleteView, generic_UserList, generic_ProductList, ListProductsMixins, DetailProductMixins, ListProductsGenerics, DetailProductGenerics, DetailCreateProductGenerics , ProductListCreateAPIView


from app_product.views import ProductViewSet,ProductCategoryViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register('productviewset',ProductViewSet,basename='product')
router.register('productcategoryviewset',ProductCategoryViewSet,basename='productcategory')

 
app_name ='app_product'


urlpatterns = [
    # funcion based
    path('product-dashboard/',views.listproducts, name='product-dashboard'),

    path('product-addrecord/',views.product_addrecord, name='product-addrecord'),

    # for  test purposes

    path('api-product-list/',views.api_ProductList, name='api-product-list'),

    
    path('api-list-messages/',views.ListMessages, name='api-list-messages'),

    # class based ApiView
    path('apiclass-ProductView/',apiclass_ProductView.as_view(), name='apiclass-ProductView'),

    path('apiclassProductDetailView/<int:pk>',apiclass_ProductDetailView.as_view(), 
    name='apiclassProductDetailView'),

    
    path('apiclass-ProductUpdateView/<int:pk>',apiclass_ProductUpdateView.as_view(), name='apiclass-ProductUpdateView'),
    path('apiclass-ProductDeleteView/<int:pk>',apiclass_ProductDeleteView.as_view(), name='apiclass-ProductDeleteView'),

    # generic view
    path('generic-UserList/',generic_UserList.as_view(), name='generic-UserList'),


    path('generic-ProductList/',generic_ProductList.as_view(), name='generic-ProductList'),
    
    #  call requests to get from api (function view)
    path('listproducts2/',views.listproducts2, name='listproducts2'),

    ## using mixins
    path('mixins-path/',ListProductsMixins.as_view(), name='mixins-listproducts'),



    path('detailed-mixins/<int:pk>',DetailProductMixins.as_view(), name='detailed-mixins'),
    #---------- django generic crud-----------------

    path('generic-product/',ListProductsGenerics.as_view(), name='generic-product'),
    
    path('generic-detailproduct/<int:pk>',DetailProductGenerics.as_view(), name='generic-detailproduct'),

    path('generic-detailcreateproduct/',DetailCreateProductGenerics.as_view(), name='generic-detailcreateproduct'),

    path('ProductListCreateAPIView/',ProductListCreateAPIView.as_view(), name='ProductListCreateAPIView'),


    
#---------- viewsets -----------------

  ]+router.urls