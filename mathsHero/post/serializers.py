from rest_framework import serializers
from ans_post.models import Post

class PostSerializer(serializers.ModelSerializer):
    def __str__(self):
        pass

    class Meta:
        model = Post
        fields = '__all__'