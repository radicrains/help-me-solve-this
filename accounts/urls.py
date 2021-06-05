from django.urls import path
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path('',home_view, name='home'),
    path('register/', register_view, name ='user_register'),
    # path('', register_view, name ='register'),
    path('login/', login_view, name ='user_login'),
    path('logout/', logout_view, name='user_logout')
]