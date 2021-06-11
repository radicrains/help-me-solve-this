from django.urls import path
from .views import *

app_name = "questions"

urlpatterns = [
    path('', view_index, name='questions_index'),
    path('create/', view_question_create, name='questions_create'),
    path('category/', view_category, name='category'),
    path('show/<uuid:pk>', view_show, name='question_show'),
    # path('like/<uuid:pk>', like_qns, name="like_question"),
    path('userqns/', view_qns_by_user, name='question_user')
    
    # path('category/<uuid:pk' view_category_filter, name='category_filter')
]