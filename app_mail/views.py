from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.shortcuts import render
from app_mail.models import EmailDB, EmailANS
from app_articles.models import  User
from accounts.models import UserAccess
from app_mail.forms import Email_Answer, CreateEmailForm, ResponseEmail
from . utils import send_email,send_response_email
from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from accounts.utils import is_ajax
from app_mail.forms import Email_Answer
from django.contrib.auth.decorators import login_required, permission_required

from app_product.models import Product
from app_product.mydecorator import custom_permission_required




#-=------- testsample

@login_required(login_url='accounts:login-view')
def email_me(request):
  user = UserAccess.objects.get(user=request.user)
  if request.method=='POST':
    form = CreateEmailForm(request.POST)
    if form.is_valid():
      instance=form.save(commit=False)
      instance.email_from =user.user.email
      instance.email_to=settings.DEFAULT_FROM_EMAIL
      instance.user = request.user
      instance.save()
      mail_subject= 'Inquiries for Rent' 
      email_template = 'app_mail/email/inquiry_email.html'
      email_body = form.cleaned_data['email_body']
      if user.send_email_trigger :
        send_email(request,mail_subject,email_template, email_body)
      return redirect('home')
  else:
    form=CreateEmailForm()
  context={'form':form,}
  return render(request,'app_mail/email_me.html', context )  



# @permission_required("app_mail.delete_emaildb",login_url='home', raise_exception=False)
@custom_permission_required("app_mail.delete_emaildb")
@login_required(login_url='accounts:login-view')
def email_list(request):
  emails= EmailDB.objects.all() 
  if request.method=='POST':
    form = ResponseEmail(request.POST)
    if form.is_valid():
      instance=form.save(commit=False)
      instance.email_from = settings.DEFAULT_FROM_EMAIL
      instance.email_to = form.cleaned_data['email_to']
      # instance.user = request.user
      instance.save()
      response_to = form.cleaned_data['email_to']
      mail_subject= 'Response from Inquiry' 
      email_template = 'app_mail/email/inquiry_response.html'
      email_body = form.cleaned_data['email_body']
      send_response_email(request,mail_subject,email_template, email_body,response_to)
      return redirect('home')
  else:    
    form=ResponseEmail()
  context={'form':form,'emails':emails}
  return render(request,'app_mail/email_list.html', context )  

@custom_permission_required("app_mail.delete_emaildb")
@login_required(login_url='accounts:login-view')
def email_list_view(request):
  emails=EmailDB.objects.filter(replied=False)
  form = Email_Answer()
  user = UserAccess.objects.get(user=request.user)
  if request.method=='POST':
    form=Email_Answer(request.POST)
    if form.is_valid():
      email_from      = settings.EMAIL_HOST_USER
      email_to        = request.POST.get('form_data_emailto')
      email_body      = request.POST.get('form_data_body')
      package_amount  = request.POST.get('form_data_amount')
      if user.send_email_trigger :
        send_email_to_queries (request,email_from,email_to,email_body,package_amount)  
      else :
        print(f'\nReply to query -> sending email :trigger is off')   
      instance = EmailANS.objects.create(
        email_from = email_from, 
        email_to = email_to, 
        email_body=email_body ,

        email_ref_id=request.POST.get('sid'),

        package_amount = package_amount
      
        )
      instance.save()
      sid_id =request.POST.get("sid")
      emaildb=EmailDB.objects.get(pk=sid_id)
      emaildb.replied=True
      emaildb.save()
      return JsonResponse({"status": 1})
    
  context = {'emails':emails, 'form':form}
  return render(request,'app_mail/email_list_view.html', context )

@login_required(login_url='accounts:login-view')
def send_email_to_queries (request,email_from,email_to,email_body,package_amount)   :
      response_to = email_to
      mail_subject= 'Response from Inquiry' 
      email_template = 'app_mail/email/inquiry_response.html'
      email_body =email_body
      send_response_email(request,mail_subject,email_template, email_body,response_to,package_amount)

@login_required(login_url='accounts:login-view')
def reply_email(request):
  if request.method=='POST':
    id =request.POST.get("sid")
    emaildb=EmailDB.objects.get(pk=id)
    emaildb.replied=True
    emaildb.save()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})

@login_required(login_url='accounts:login-view')
def emailin_delete(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    email = EmailDB.objects.get(pk=id)
    email.delete()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})  

@login_required(login_url='accounts:login-view')
def answered_email_toggle (request) :
  
  if request.method == "POST":  
    id = request.POST.get("stuid")
    email = EmailDB.objects.get(pk=id)
    email.replied=False
    email.save()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})  

@login_required(login_url='accounts:login-view')
def answered_email(request):
  email_ans = EmailANS.objects.all().order_by('-created_date')
  
  context={'email_ans':email_ans}
  return render(request,'app_mail/answered_email.html', context )


def email_reply(request)  :
  pass
