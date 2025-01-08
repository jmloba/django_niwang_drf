from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings

from django.core.validators import RegexValidator

#validators
def regex_validators_alpha():
  alpha_only = RegexValidator(r"^[a-zA-Z\- ]*$", message='Alpha only ^^^')
  return alpha_only
def regex_validators_numberonly():
  numeric_char = RegexValidator(r"^[0-9]+$", message='only numbers are allowed')
  return numeric_char

def regex_validators_alphanumeric():
  numeric_char = RegexValidator(r"^[a-z\d\-_\s]+$",message='only AlphaNumeric are allowed')
  return numeric_char

def regex_validators_philmobile():
  philmobile = RegexValidator(r'09\d\d-\d\d\d-\d\d\d\d$',message= 'follow pattern 09xx-xxx-xxxx')
  return philmobile

def regex_validators_xx():
  x = RegexValidator(r'09\d\d-\d\d\d-\d\d\d\d$',message= 'follow pattern 09xx-xxx-xxxx')
  return x
def regex_validators_DC():
  x = RegexValidator(r"^[DdCc]+$", 'D or C')
  return x

def detectUser(user):
  if user.role == 1:
    redirectUrl ='dashboardVendor'
  elif  user.role == 2:
    redirectUrl ='dashboardCustomer'
  elif  user.role == None and user.is_superadmin:
    redirectUrl ='/admin'

  return redirectUrl

def reformat_date(val):
  print(f'reformatting val: {val}')
  #  abbreviated month %b
  #  abbreviated full month %B
  # val = val.strftime("%B %d, %Y, %H:%M ")
  # val = val.strftime("%B %d, %Y, %I:%M %p")
  val = val.strftime("%Y/%m/%d, %I:%M %p")
  return val

def formatdate_YYYYMMDD(val):
  print(f'reformatting val: {val}')
  #  abbreviated month %b
  #  abbreviated full month %B
  # val = val.strftime("%B %d, %Y, %H:%M ")
  # val = val.strftime("%B %d, %Y, %I:%M %p")
  val = val.strftime("%Y/%m/%d, %I:%M %p")
  return val






def send_verification_email(request,user,mail_subject,email_template):
  print(f'inhside send_verification_email')
  from_email = settings.DEFAULT_FROM_EMAIL
  print(f'from email: {from_email}')
  current_site = get_current_site(request) 
 
  message =render_to_string(email_template,      
        {
        'user':user,
        'domain': current_site,
        # encode users primary key -> user.pk
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user)      }
        )
  to_email = user.email
    

  mail = EmailMessage(mail_subject,message, to=[to_email])
  mail.send()
  print('------?>>>>>>>>>>     mail sent')


# called form vendor models
def send_notification(mail_subject, mail_template, context):
  from_email = settings.DEFAULT_FROM_EMAIL
  message =render_to_string(mail_template,     context )
  to_email = context['user'].email
  mail = EmailMessage(mail_subject,message, to=[to_email])
  mail.send()

  return

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def reformat_date(val):
  print(f'reformatting val: {val}')
  #  abbreviated month %b
  #  abbreviated full month %B
  # val = val.strftime("%B %d, %Y, %H:%M ")
  # val = val.strftime("%B %d, %Y, %I:%M %p")
  val = val.strftime("%Y/%m/%d, %I:%M %p")
  return val

def date_format2(val):
  print(f'reformatting val: {val}')
  #  abbreviated month %b
  #  abbreviated full month %B
  # val = val.strftime("%B %d, %Y, %H:%M ")
  # val = val.strftime("%B %d, %Y, %I:%M %p")
  val = val.strftime("%Y/%m/%d" )
  return val




