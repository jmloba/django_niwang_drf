from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

from .models import UserProfile, UserAccess



class UserForm(forms.ModelForm):
  password         = forms.CharField(widget=forms.PasswordInput())
  confirm_password = forms.CharField(widget=forms.PasswordInput())
  class Meta:
    model = User
    fields=['first_name','last_name','username','email','password']
  def clean(self):
    cleaned_data = super(UserForm,self).clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')
    if password != confirm_password:

      raise forms.ValidationError('Password does not match')
    
class CreateUserForm(UserCreationForm):
  class Meta:
    model=User
    fields=['username','email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ('location','age')

class UserAccessForm(forms.ModelForm):
  class Meta:
    model=UserAccess
    fields=()    