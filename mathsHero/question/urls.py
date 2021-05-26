from django.urls import path
from .views import *

app_name = "questions"

urlpatterns = [
    path('', view_index, name='questions_index'),
    path('show/<uuid:pk>', view_show, name='question_show'),
    # path('category/<uuid:pk' view_category_filter, name='category_filter')
    path('category/', view_category_create, name='category_create'),
    # path('series/', view_create_series, name='series_create'),
    # path('series/<uuid:pk>', view_series, name='series_view')
]