
from django.contrib import admin
from app_product import views
from django.urls import include, re_path,path
from app_product.views import apiclass_ProductView, apiclass_ProductDetailView, apiclass_ProductUpdateView,apiclass_ProductDeleteView, generic_UserList, generic_ProductList




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
    path('apiclass-ProductDetailView/<int:pk>',apiclass_ProductDetailView.as_view(), name='apiclass-ProductDetailView'),
    path('apiclass-ProductUpdateView/<int:pk>',apiclass_ProductUpdateView.as_view(), name='apiclass-ProductUpdateView'),
    path('apiclass-ProductDeleteView/<int:pk>',apiclass_ProductDeleteView.as_view(), name='apiclass-ProductDeleteView'),

    # generic view
    path('generic-UserList/',generic_UserList.as_view(), name='generic-UserList'),


  path('generic-ProductList/',generic_ProductList.as_view(), name='generic-ProductList'),

path('generic-getProductList/',views.listproducts2, name='generic-getProductList'),

  ]