from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.shortcuts import render
from app_mail.models import EmailDB, EmailANS
from app_articles.models import  User
from accounts.models import UserAccess
from .forms import Email_Answer, CreateEmailForm, ResponseEmail
from . utils import send_email,send_response_email
from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from accounts.utils import is_ajax
from app_mail.forms import Email_Answer

# Create your views here.
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
      else : 
        
        print(f"\nNo email sent !!! \n useraccess -> send_email_trigger : {user.send_email_trigger} ")  
      return redirect('home')
  else:
    form=CreateEmailForm()
  context={'form':form,}
  return render(request,'app_mail/email_me.html', context )  

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
      print(f'sending to {response_to} ')
      send_response_email(request,mail_subject,email_template, email_body,response_to)
      return redirect('home')
  else:    
    form=ResponseEmail()
  context={'form':form,'emails':emails}
  return render(request,'app_mail/email_list.html', context )  

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

      print (f'***request email : {email_to}')
      print (f'***request body : {email_body}')
      print (f'***request amount : {package_amount}')
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

      print(f'returning status 1')
      return JsonResponse({"status": 1})
    
  context = {'emails':emails, 'form':form}
  return render(request,'app_mail/email_list_view.html', context )

def send_email_to_queries (request,email_from,email_to,email_body,package_amount)   :
      response_to = email_to
      mail_subject= 'Response from Inquiry' 
      email_template = 'app_mail/email/inquiry_response.html'
      email_body =email_body
      print(f'sending to {response_to} ')

      send_response_email(request,mail_subject,email_template, email_body,response_to,package_amount)

def reply_email(request):
  print('pass  reply_email')
  pass
  if request.method=='POST':
    id =request.POST.get("sid")
    emaildb=EmailDB.objects.get(pk=id)
    emaildb.replied=True
    emaildb.save()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})


def emailin_delete(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    email = EmailDB.objects.get(pk=id)
    print(f'email to delete : {email}')
    email.delete()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})  


def answered_email_toggle (request) :
  print(f'views answered email toggle')
  if request.method == "POST":  
    id = request.POST.get("stuid")
    print(f' text')
    email = EmailDB.objects.get(pk=id)
    email.replied=False
    email.save()
    print(f'\n\n--->>>>email--saved')


    return JsonResponse({"status": 1})
  else:
    print(f'views answered email toggle: reque3st is not post')
    return JsonResponse({"status": 0})  


def email_reply(request)  :
  pass

def answered_email(request):
  email_ans = EmailANS.objects.all().order_by('-created_date')
  
  context={'email_ans':email_ans}
  return render(request,'app_mail/answered_email.html', context )

