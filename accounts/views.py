from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm
from allauth.account.models import EmailAddress

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
            EmailAddress.objects.add_email(request, user, user.email, signup=True, confirm=True)
            return redirect('accounts:check_email')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def check_email(request):
    return render(request, 'accounts/check_email.html')

def email_confirm(request):
    return render(request, 'accounts/email_confirm.html')


def sign_out(request):
    logout(request)
    return redirect('store:home')
