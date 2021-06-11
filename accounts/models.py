from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, User
from django.urls.base import reverse

# Create your models here.
class User(AbstractUser):
    pass

class Profile(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse("profile_show","other_profile_show",kwargs={"pk": self.pk, "user.id":self.user.id})