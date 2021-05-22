from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

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

