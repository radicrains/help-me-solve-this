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
@permission_classes([AllowAny])
def register_view(request):
    if request.method == 'POST':
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response({ 'message': 'user registered!'})
        else:
            return Response({ 'message': 'user not registered!'})