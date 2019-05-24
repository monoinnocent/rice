from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    return render(request, 'employee/login.html')

def forgetpassword(request):
    return render(request, 'employee/forgetpassword.html')

def homedashboard(request):
    return render(request, 'employee/home-dashboard.html')

def user(request):
    return render(request, 'employee/user.html')

def useredit(request):
    return render(request, 'employee/user-edit.html')
