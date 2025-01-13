from django import forms
from app_blog.models import BlogPost


class  PostForm(forms.ModelForm):
  class Meta :
    model = BlogPost
    fields=('title','description',
           
            )    
