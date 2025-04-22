from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('store:home')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/sign_in.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('store:home')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('store:home')
