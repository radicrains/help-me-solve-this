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
    
    description = models.TextField()
    # image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    # categories = models.ManyToManyField(Category, related_name='posts')

    # meta information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
