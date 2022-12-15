from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"hello/index.html")


def nome(request, nome):
    return render(request,"hello/nome.html",{"name":nome.title()})