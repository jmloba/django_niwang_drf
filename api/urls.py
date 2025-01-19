
from django.urls import include, re_path,path
from api.views import DetailArticleMixin,ListArticlesMixins, generic_UserList, generic_ProductList, DetailProductMixins, ListProductsGenerics, DetailProductGenerics, DetailCreateProductGenerics, ProductListCreateAPIView, PremiumProducts, ListProductsMixins, BlogPostCreate,BlogPostRetreiveUpdateDestroy

app_name='api'
from api import views

urlpatterns = [
  # blogpost
      path('blogpost/',BlogPostCreate.as_view(), name='BlogPost'),

      path('blogpost/<int:pk>',BlogPostRetreiveUpdateDestroy.as_view(), name='BlogPostRUD'),

    
    path('articledetailMixin/<int:pk>',DetailArticleMixin.as_view(), name='articledetailMixin'),

    
    path('articleListMixin/',ListArticlesMixins.as_view(), name='articleListMixin'),

    path('api-product-list/',views.api_ProductList, name='api-product-list'),
    path('generic-UserList/',generic_UserList.as_view(), name='generic-UserList'),

    
    path('generic-ProductList/',generic_ProductList.as_view(), name='generic-ProductList'),
    
    path('detailed-mixins/<int:pk>',DetailProductMixins.as_view(), name='detailed-mixins'),
   #---------- django generic crud-----------------

    path('generic-product/',ListProductsGenerics.as_view(), name='generic-product'),
 
    path('generic-detailproduct/<int:pk>',DetailProductGenerics.as_view(), name='generic-detailproduct'),        


    path('generic-detailcreateproduct/',DetailCreateProductGenerics.as_view(), name='generic-detailcreateproduct'),

  path('ProductListCreateAPIView/',ProductListCreateAPIView.as_view(), name='ProductListCreateAPIView'),

  path('premiumProducts/',PremiumProducts.as_view(), name='premiumProducts'),  
  path('mixins-path/',ListProductsMixins.as_view(), name='mixins-listproducts'),
]