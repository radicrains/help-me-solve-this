from django.urls import path
from .views import *

app_name = 'answers'

urlpatterns = [
    path('post/<uuid:pk>', view_answers_create, name='question_answer'),
    #  path("", views.views_index, name='reviews_index')
    # path("<uuid:question_id>", view_reviews, name='ans_index')
]

