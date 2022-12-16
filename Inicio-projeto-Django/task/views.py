from django.shortcuts import render

# Create your views here.

tasks = []

def createtask(request):
    return render(request,"task/index.html")

def addtask(request):
    task = request.POST.get("input-task")
    tasks.append(task)

    return render(request, 'task/index.html', {"tasks": tasks}) 