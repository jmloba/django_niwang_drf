from django.db import models

# Create your models here.

class ProductCategory(models.Model):
  categoryname = models.CharField(max_length=50, unique=True)
  category_id = models.PositiveBigIntegerField(unique=True)
  
  verbose_name='Product Category'
  def __str__(self):
    return self.categoryname



class Product(models.Model):
  category_name = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='ProductCategory',null=True, blank=True)


  product_id = models.CharField(max_length=20, null=True, blank=True, unique=True)
  
  name=models.CharField(max_length=50)

  cost = models.DecimalField(max_digits =8 ,decimal_places=2,null=True, blank=True)
  date = models.DateField()
  
  description = models.TextField(max_length=200, null=True, blank=True)

  def  __str__(self):
    return self.name

