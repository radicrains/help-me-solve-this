from django.urls import path
from .views import *

app_name = "questions"

urlpatterns = [
    path('', view_index, name='questions_index'),
    path('show/<uuid:pk>', view_show, name='question_show'),
    path('category/create', view_category_create, name='category_create'),
    # path('category/<uuid:pk' view_category_filter, name='category_filter')
]