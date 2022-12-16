from django.urls import path
from . import views

urlpatterns = [
    path("",views.resposta,name="respota-ano-novo")
]