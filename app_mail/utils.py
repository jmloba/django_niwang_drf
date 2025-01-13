from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings



def send_email(request,mail_subject,email_template,email_body):
  to_email = settings.DEFAULT_FROM_EMAIL 
  from_email = request.user.email
  firstname = request.user.first_name
  lastname = request.user.last_name
  mail_subject = "Niwang.com : Inquiries for rent"
  message =render_to_string(email_template,  {
    'email_body':email_body,
    'from_email': from_email, 
    'firstname':firstname,
    'lastname':lastname, 
    'mail_subject':mail_subject
    } )
    
  mail = EmailMessage(mail_subject,message, to=[to_email] )
  mail.send()

def send_response_email(request,mail_subject,email_template,email_body,response_to,package_amount):
  to_email = response_to
  from_email =  settings.DEFAULT_FROM_EMAIL
  firstname = request.user.first_name
  lastname = request.user.last_name
  mail_subject = "Response to your inquiry"
  
  message =render_to_string(email_template,  {
    'email_body':email_body,
    'from_email': from_email, 
    'firstname':firstname,
    'lastname':lastname, 
    'mail_subject':mail_subject,
    'response_to': response_to,
    'package_amount':package_amount

    } )
    
  mail = EmailMessage(mail_subject,message, to=[to_email] )
  mail.send()
