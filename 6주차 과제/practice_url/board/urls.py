from board import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.board),
    path('first/',views.boardfirst)
]
