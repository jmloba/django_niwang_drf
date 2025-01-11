from django import forms
from app_articles.models import Article


class DateInput(forms.DateInput):
  input_type = 'date'

class ArticleForm(forms.ModelForm):

  class Meta :
    model = Article
    fields=('title','body','thumb'
           
            )    

class CreateArticleForm(forms.ModelForm):
  class Meta :
    model = Article
    fields= ('title','body', 'thumb' )
    widget ={
      'title': forms.TextInput(attrs={"class":"form-control"}),
      'body': forms.Textarea(attrs={"class":"form-control"}),
      'thumb': forms.ClearableFileInput(attrs={
        'class':'form-control'
      })
    }