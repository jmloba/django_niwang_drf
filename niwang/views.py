
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User 

from .serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile, UserAccess

@login_required(login_url='accounts:login-view')
def home(request):
  totalrecords=len(User.objects.all())
  print(f'total records:  {totalrecords}')
  context = {'totalrecords':totalrecords  }
  return render(request,'home.html',context )


@api_view(['POST'])
def login(request):
  user = get_object_or_404(User, username=request.data['username'])
  if not user.check_password(request.data['password']):

    return Response({"detail":"not found"}, status=status.HTTP_400_BAD_REQUEST )
  token, created = Token.objects.get_or_create(user=user)
  serializer = UserSerializer(instance=user)
  response={"token": token.key, "user": serializer.data}

  return Response (response)


@api_view(['POST'])
def signup(request):
  serializer = UserSerializer(data= request.data)
  if serializer.is_valid():
    serializer.save()

    user = User.objects.get(username = request.data['username'])
    # note set_password to hash the password
    user.set_password(request.data['password'])
    user.save()

    token = Token.objects.create(user=user)
    userprofile = UserProfile.objects.create(user=user)

    useraccess = UserAccess.objects.create(user=user)
    
    response = {"token" : token.key, "user":serializer.data}
    return Response(response)
  # when serializer is not valid
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
  response = "passed for {}".format(request.user.email)
  return Response (response)

#----
from rest_framework.views import APIView
from django.contrib.auth import authenticate

class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
  