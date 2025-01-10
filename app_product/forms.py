from django import forms
from app_product.models import Product


class DateInput(forms.DateInput):
  input_type = 'date'

class ProductForm(forms.ModelForm):
  date = forms.DateField(
    widget = forms.DateInput(
      attrs={
        'class':'form-control', 
        'type': 'date',
      }
    )
  )
  class Meta :
    model = Product
    fields=('product_id','name','cost','date',
            'description',
           
            )    



