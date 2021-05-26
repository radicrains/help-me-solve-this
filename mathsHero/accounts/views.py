from accounts.models import User, Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm

def home_view(request):
    return render(request, 'accounts/home.html')

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
            profile = Profile(user=user)
            profile.save()
        except IntegrityError:
            messages.error(request, "Username is taken already")
            return render(request, 'accounts/register.html')

        login(request, user)
        messages.success(request, "Registration successful." )
        return redirect("accounts:user_login")
    else:
        messages.error(request, "Unsuccessful registration. Invalid information.")
        form = UserCreationForm()
        return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("questions:questions_index")
        else:
            messages.error(request, "username or password is incorrect")
            return render(request, "accounts/login.html")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    #NOTETOSELF - REDIRECT TO HOME PAGE
    return redirect('accounts:login')
