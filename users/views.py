from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *


def login_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, 'Successfully Logged In!')
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def user_signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Successfully Registered!')
        return redirect('index')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'users/signup.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'You Logged Out!')
    return redirect('index')
