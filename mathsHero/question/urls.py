from django.urls import path
from .views import *

app_name = "questions"

urlpatterns = [
    path('', view_index, name='questions_index'),
    # path('show/<uuid:pk>', view_show, name='book_show'),
    # path('category/', view_create_category, name='category_create'),
    # path('series/', view_create_series, name='series_create'),
    # path('series/<uuid:pk>', view_series, name='series_view')
]