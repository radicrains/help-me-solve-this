from accounts.models import User, Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    pass