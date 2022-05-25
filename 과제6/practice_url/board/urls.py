from django.urls import path
from board import views

urlpatterns = [
    path('', views.board),
    path('firs/', views.boardfirst)
]
