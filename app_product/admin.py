from django.contrib import admin
from app_product.models import Product, ProductCategory
# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
  list_display=('categoryname','category_id',)
  ordering=('categoryname',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class ProductAdmin(admin.ModelAdmin):
  list_display=('product_id','name','category_name','cost','date','description')
  ordering=('name',)
  list_editable =('name','category_name','cost','date','description',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

admin.site.register(Product,ProductAdmin )  
admin.site.register(ProductCategory,ProductCategoryAdmin )  
