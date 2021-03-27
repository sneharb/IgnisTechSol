from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="main"),
    path('register/', views.register, name="register")
]
