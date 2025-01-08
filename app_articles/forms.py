from django import forms
from app_articles.models import Article


class DateInput(forms.DateInput):
  input_type = 'date'

class ArticleForm(forms.ModelForm):

  class Meta :
    model = Article
    fields=('title','body','thumb'
           
            )    

