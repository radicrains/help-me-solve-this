from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ans_post.models import *
from ans_post.serializers import *



# Create your views here.

@api_view(['GET', 'POST'])
def view_index(request):
    # return Response({'message': 'it works'})

    #if GET request to show all the posts
    # if request.method == 'GET':
        
    
    #else if POST request, to save the input post.
    if request.method == 'POST':
        post = PostSerializer(data = request.data)
        if post.is_valid():
            post.save()
            return Response({'message': 'Post is saved!'})
        else:
            print(post.errors)
            # return Response({'message': 'Post is saved!'})

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many = True)
    return Response(serializer.data)
