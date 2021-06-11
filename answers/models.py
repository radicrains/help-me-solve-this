from django.db import models
import uuid
from accounts.models import *
from question.models import *
from cloudinary.models import CloudinaryField

# Create your models here.

class Answer(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    
    name = models.ForeignKey(User, related_name="answers_user",
                             on_delete=models.DO_NOTHING)
    answer = models.TextField(null=True)
    ansimg = CloudinaryField('image')
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers_qn')

    verify = models.ManyToManyField(User, related_name='ans_post')

    def serialize(self):
        return {
            "id": self.id,
            "user": {
                "username": self.name.username
            },
            "answer": {
                "answer":self.answer,
                "ansimg":self.ansimg
            },
            "question": {
                "title": self.question.title,
                'id': self.question.id
                # "categories": self.question.categories
            }
        }
