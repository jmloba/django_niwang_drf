from django.shortcuts import render


# Create your views here.


def membersDashboard(request):
  context = {}
  template = 'app_members/membersDashboard.html'
  return render(request,template,context)

