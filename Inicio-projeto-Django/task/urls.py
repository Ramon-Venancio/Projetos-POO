from django.urls import path
from . import views

urlpatterns = [
    path("",views.createtask,name="task"),
    path("addtask/",views.addtask,name="adicionar_task")
]