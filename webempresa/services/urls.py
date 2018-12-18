from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 
    #path del core

    path('',views.services,name='services'),


]
