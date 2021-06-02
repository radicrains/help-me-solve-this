from django.urls import path
from .views import *

app_name = "questions"

urlpatterns = [
    path('', view_index, name='questions_index'),
    path('create/', view_question_create, name='questions_create'),
    path('category/create', view_category_create, name='category_create'),
    path('show/<uuid:pk>', view_show, name='question_show'),
    # path('answer/<uuid:pk>', view_answers_create, name='question_answer')
    
    # path('category/<uuid:pk' view_category_filter, name='category_filter')
]