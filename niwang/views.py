


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.utils.timezone import localdate
from django.db.models import Sum,Count 
from django.contrib.auth.models import User, Group





def home(request):
  totalrecords=len(User.objects.all())
  print(f'total records:  {totalrecords}')
  context = {'totalrecords':totalrecords  }
  return render(request,'home.html',context )
