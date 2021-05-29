from django.urls import path
from .views import *
# from .views import views_index
# from . import views

app_name = 'answers'

urlpatterns = [
    path("post/<uuid:question>", views_create, name='ans_create'),
    #  path("", views.views_index, name='reviews_index')
    path("<uuid:question_id>", view_reviews, name='ans_index')
]

