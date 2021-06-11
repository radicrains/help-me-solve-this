from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import *


app_name = "accounts"

urlpatterns = [
    path('',home_view, name='home'),
    path('register/', register_view, name ='user_register'),
    path('profile/', user_update_view, name ='user_profile'),
    path('password/',auth_views.PasswordChangeView.as_view(template_name='accounts/change-password.html')),
    path('password_success/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_success.html')),
    path('login/', login_view, name ='user_login'),
    path('logout/', logout_view, name='user_logout'),
    
]