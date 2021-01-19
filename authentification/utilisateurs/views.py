from django.shortcuts import render, redirect
from . import models
from sms import Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('******************************************************', email, password )
        user = authenticate(email=email, password=password)
        if user is not None and user.is_active :
            login(request, user)
            return redirect('profile')
        else:
            return redirect('login')
    return render(request, 'pages/login.html')


def register(request):
    if request.method == "POST" :
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if password == repassword :
            user = User()
            user.email = email
            user.username = email
            user.password = password
            user.set_password(user.password)
            user.save()
            print('OK OK OK OK OK OK')
        
    return render(request, 'pages/register.html')



def profile(request):
    
    return render(request, 'pages/profile.html')