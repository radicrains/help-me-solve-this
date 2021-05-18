# from rest_framework.response import Response
# from rest_framework.decorators import api_view
from ans_post.models import *
from ans_post.forms import *
# from ans_post.serializers import *
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import uuid



# Create your views here.

# @api_view(['GET', 'POST'])
@login_required
def view_index(request):
    # return Response({'message': 'it works'})

    #if GET request to show all the posts
    # if request.method == 'GET':
        # posts = Post.objects.all()
        # serializer = PostSerializer(posts, many = True)
    
    #else if POST request, to save the input post.
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():

            post = Post(title = request.POST['title'],
                        description = request.POST['description'],
                        image = request.POST['image']
                    )

            post.save()
            categories = form.cleaned_data['categories']

            for cat in categories:
                post.categories.add(cat)
            return redirect('post:post_index')
        posts = Post.objects.all()
        context = {'form': form, 'posts': posts}
        return render (request, 'ans_post/index.html', context)
        # else:
        #     print(post.errors)
            # return Response({'message': 'Post is saved!'})

    # posts = Post.objects.all()
    # serializer = PostSerializer(posts, many = True)
    # return Response(serializer.data)
