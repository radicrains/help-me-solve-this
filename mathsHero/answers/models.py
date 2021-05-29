from accounts.models import *
from question.models import *
from django.db import models
import uuid

# Create your models here.


class Answer(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    
    name = models.ForeignKey(User, related_name="answers",
                             on_delete=models.DO_NOTHING)
    ans_cover = CloudinaryField('image')
    ans_description = models.TextField(null=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')

    def serialize(self):
        return {
            "id": self.id,
            "user": {
                "username": self.name.username
            },
            "answer": self.answer,
            "post": {
                "title": self.question.title,
                "categories": self.question.categories
            }
        }
