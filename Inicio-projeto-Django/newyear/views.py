from django.shortcuts import render
from datetime import datetime as dt

# Create your views here.

def resposta(request):
    now = dt.now()
    return render(request,"newyear/index.html",{
        "newyear": now.month==1 and now.day==1
    })