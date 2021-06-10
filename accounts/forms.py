from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Profile
from django.contrib.auth.forms import UserChangeForm


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'
        exclude = (
            'last_login',
            'groups',
            'user_permissions',
            'first_name',
            'last_name',
            'is_staff',
            'date_joined',
            'is_superuser',
            'is_active',
            'password',
        )

# class SuperUserUpdateForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = '__all__'
#         exclude = (
#             'last_login',
#             'groups',
#             'user_permissions',
#             'first_name',
#             'last_name',
#             'is_staff',
#             'date_joined',
#         )

# class ProfileUpdate(forms.ModelForm):
#     class Meta:
#         model = Profile
        # fields = '__all__'