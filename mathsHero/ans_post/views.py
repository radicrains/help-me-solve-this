from ans_post.models import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import uuid

# Create your views here.

@api_view(['GET'])
def view_index(request):
    return Response({'message': 'it works'})
