from django.db import models
import uuid
from accounts.models import *
# from django.urls.base import reverse
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class Question(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField()
    # ImageField needs pillow to run
    # cover = models.ImageField(upload_to='uploads/%Y/%m/%d')
    cover = CloudinaryField('image')
    user = models.ForeignKey(User, default='', null=True, related_name='user_posts', on_delete=models.CASCADE)
   
    categories = models.ManyToManyField(Category, related_name='category_name')
    likes = models.ManyToManyField(User, related_name='qns_post')

    # meta information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("question_show", kwargs={"pk": self.pk})


# class Answer(models.Model):
#     id = models.UUIDField(  # new
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False)
    
#     name = models.ForeignKey(User, related_name="answers_user",
#                              on_delete=models.DO_NOTHING)
#     answer = models.TextField(null=True)
#     ansimg = CloudinaryField('image')
#     question = models.ForeignKey(
#         Question, on_delete=models.CASCADE, related_name='answers_qn')

#     def serialize(self):
#         return {
#             "id": self.id,
#             "user": {
#                 "username": self.name.username
#             },
#             "answer": {
#                 "answer":self.answer,
#                 "ansimg":self.ansimg
#             },
#             "question": {
#                 "title": self.question.title,
#                 'id': self.question.id
#                 # "categories": self.question.categories
#             }
#         }