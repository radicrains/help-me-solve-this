from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserChangeForm

# class AccountRegistration(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = Userfields = ['username','email','password1','password2']

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
        )

# class ProfileUpdate(forms.ModelForm):
#     class Meta:
#         model = Profile
        # fields = '__all__'