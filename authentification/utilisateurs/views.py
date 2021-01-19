from django.shortcuts import render
from . import models
from sms import Message
# Create your views here.

def login(request):
    return render(request, 'pages/login.html')


def register(request):
    return render(request, 'pages/register.html')




def profile(request):
    
    return render(request, 'pages/profile.html')