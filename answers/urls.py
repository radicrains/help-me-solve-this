from django.urls import path
from .views import *

app_name = 'answers'

urlpatterns = [
    path('answer/<uuid:pk>', view_answers_create, name='question_answer'),
]

