from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def welcome(request):
    return render(request, 'unauth/index.html')


def gotoLogin(request):
    return redirect('unauth:login')

def gotoRegister(request):
    return redirect('unauth:register')


def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            login(request, user)
            return redirect('main:index')
    else:
        form = LoginForm()
    return render(request, 'unauth/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unauth:w_home')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'unauth/register.html', args)
# Create your views here.
