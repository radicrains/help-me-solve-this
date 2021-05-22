from django.urls import path
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path('register/', register_view, name ='register'),
    path('login/', login_view, name ='login'),
    path('private/', private_view, name ='private')
]