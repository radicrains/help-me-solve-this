from django.db import models
import uuid
from django.urls.base import reverse
# Create your models here.
class Post(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    title = models.CharField(max_length=200, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    categories = models.ManyToManyField(Category, related_name='posts')

    # meta information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("post_show", kwargs={"pk": self.pk})

class Category(models.Model):
 
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=200, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
