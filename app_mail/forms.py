from django.forms import Textarea, TextInput
from django import forms
from .models import EmailDB,EmailANS



class CreateEmailForm(forms.ModelForm):
  class Meta:
    model = EmailDB
    fields = ['email_body']

class ResponseEmail(forms.ModelForm)   :
  class Meta:
    model = EmailANS
    fields = {'email_to','email_body'}
    widget={
      "email_to": forms.Textarea(attrs={"class":"form-control",}),
      "email_body":forms.Textarea(attrs={"class":"form-control"}),
    }

class Email_Answer (forms.ModelForm):   
  class Meta:
    model=EmailANS
    fields={'email_to','email_body','package_amount'}

