from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def selldatatables(request):
    return render(request, 'sell/sell-datatables.net.html')

def sellcreate(request):
    return render(request, 'sell/sell-create.html')

def sellview(request):
    return render(request, 'sell/sell-view.html')

def sellviewcreate(request):
    return render(request, 'sell/sell-view-create.html')

def sellviewdata(request):
    return render(request, 'sell/sell-view-data.html')

def sellviewedit(request):
    return render(request, 'sell/sell-view-edit.html')

def selltimeseries(request):
    return render(request, 'sell/sell-timeseries.net.html')
