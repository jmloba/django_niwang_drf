from django import forms
from app_blog.models import Post


class  PostForm(forms.ModelForm):
  class Meta :
    model = Post
    fields=('title','description',
           
            )    
