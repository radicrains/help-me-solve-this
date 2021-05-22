from accounts.models import User, Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']

        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.error(request, "password is not a match")
            return render(request, "accounts/register.html")

        try:
            pass
            user = User.objects.create_user(username, email, password)
            # ebere2 AbstractUser
            profile = Profile(user=user)
            profile.save()
        except IntegrityError:
            messages.error(request, "Username is taken already")
            return render(request, 'accounts/register.html')

        login(request, user)
        return redirect("questions:questions_index")
    else:
        form = UserCreationForm()  # django form inbuilt
        return render(request, "accounts/register.html", {"form": form})
