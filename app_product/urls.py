
from django.contrib import admin
from app_product import views
from django.urls import include, re_path,path
from app_product.views import apiclass_ProductView, apiclass_ProductDetailView, apiclass_ProductUpdateView,apiclass_ProductDeleteView


from app_product.views import ProductViewSet,ProductCategoryViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register('productviewset',ProductViewSet,basename='product')
router.register('productcategoryviewset',ProductCategoryViewSet,basename='productcategory')

 
app_name ='app_product'


urlpatterns = [
  path('getProductList/',views.getProductList, name='getProductList'),      

    # funcion based
    path('product-dashboard/',views.listproducts, name='product-dashboard'),

    path('product-addrecord/',views.product_addrecord, name='product-addrecord'),

    path('api-list-messages/',views.ListMessages, name='api-list-messages'),

    
    path('apiclass-ProductView/',apiclass_ProductView.as_view(), name='apiclass-ProductView'),

    path('apiclassProductDetailView/<int:pk>',apiclass_ProductDetailView.as_view(), name='apiclassProductDetailView'),

    path('apiclass-ProductUpdateView/<int:pk>',apiclass_ProductUpdateView.as_view(), name='apiclass-ProductUpdateView'),

    path('apiclass-ProductDeleteView/<int:pk>',apiclass_ProductDeleteView.as_view(), name='apiclass-ProductDeleteView'),

    ## using mixins
    

  ]+router.urls