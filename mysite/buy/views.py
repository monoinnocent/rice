from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def buydatatables(request):
    return render(request, 'buy/buy-datatables.net.html')

def buycreate(request):
    return render(request, 'buy/buy-create.html')

def buyview(request):
    return render(request, 'buy/buy-view.html')

def buyedit(request):
    return render(request, 'buy/buy-edit.html')

def supdatatables(request):
    return render(request, 'buy/sup-datatables.net.html')

def supview(request):
    return render(request, 'buy/sup-view.html')

def supedit(request):
    return render(request, 'buy/sup-edit.html')
