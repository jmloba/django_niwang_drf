from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class EmailDB(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)

  
  email_from =models.CharField(max_length=50,null=True,blank=True)
  email_to =models.CharField(max_length=50,null=True,blank=True)
  email_body = models.TextField(max_length=400,null=True,blank=True)

  replied = models.BooleanField(default=False,null=True,blank=True)
  replied_date= models.DateTimeField(null=True,blank=True)

  created_date = models.DateTimeField(auto_now_add=True)



  def __str__(self):
    return str(self.email_body[:50])
  
  
class EmailANS(models.Model):  

  email_from =models.CharField(max_length=50, null=True,blank=True)
  email_to =models.CharField(max_length=50, null=True,blank=True)
  email_body = models.TextField(max_length=400, null=True,blank=True)
  email_ref_id = models.IntegerField(default=0,null=True, blank =True)
  created_date = models.DateTimeField(auto_now_add=True)
  package_amount  = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True,blank=True)
  
  def __str__(self) :
    return str(self.email_from)+str(self.email_to)

