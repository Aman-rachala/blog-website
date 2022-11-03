from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = 'index'),
    path("post/<str:name>",views.page,name = "page")
]
