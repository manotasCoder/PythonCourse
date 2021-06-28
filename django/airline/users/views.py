from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as logout_auth

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, 'users/user.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pass']
        user =  authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, 'users/login.html',{
                'context': 'invalid credentials'
            })

    return render(request, "users/login.html")

def logout(request):
    logout_auth(request)
    return render(request, "users/login.html",{
        'context':'the user has successfully log out!'
    })