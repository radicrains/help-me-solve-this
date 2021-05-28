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
    user = models.ForeignKey(User, default='', related_name='user_posts', on_delete=models.CASCADE)
   
    categories = models.ManyToManyField(Category, related_name='category_name')

    # meta information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("question_show", kwargs={"pk": self.pk})


# class Category(models.Model):
#     id = models.UUIDField(  # new
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False)
#     name = models.CharField(max_length=200, null=True)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name