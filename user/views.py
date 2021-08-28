from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


# Create your views here.


def loginView(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'User Successfully Logging')
            return redirect('index')
        else:
            messages.error(request, 'User Not found')

    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)


def RegisterView(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = form.save()
        login(request, user)
        messages.success(request, 'User Successfully Created')
        return redirect('index')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


def logoutView(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('index')
