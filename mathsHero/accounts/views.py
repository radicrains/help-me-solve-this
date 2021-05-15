from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import exceptions

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny]) #allow anyone to view
def register_view(request):
    if request.method == 'POST':
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response({ 'message': 'user registered!'})
        else:
            return Response({ 'message': 'user not registered!'})


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method == 'POST':
        User = get_user_model()

        username = request.data.get('username')
        password = request.data.get('password')

        #exceptions helps to just return error rather than stop the server (or break to code).
        #if no username or password, it will show U & P is required
        if(username is None) or (password is None):
            raise exceptions.AuthenticationFailed('Username or Password is required')
        
        #this is custom method for validation (can also be used for email validation)
        #filter the user objects by matching username and "get" the first item on the list
        user = User.objects.filter(username = username).first()

        #check for the right username & password
        if user is None:
            raise exceptions.AuthenticationFailed('User is not found')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Password is not a match')
        
        #if both username & password correct, serialized user to pass data
        serialized_user = UserSerializer(user).data

        # delete password from dict / serialized_user
        del serialized_user['password']
        
        # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/creating_tokens_manually.html
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': serialized_user
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated]) #only allow authenticated users to view
def private_view(request):
    return Response({'message' : 'Ah you see me!' })

