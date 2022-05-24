from django.urls import path
from board import views

urlpatterns = [
    # 127.0.0.1:8000/boards/의 경로
    path('', views.board),

    # 127.0.0.1:8000/boards/first/의 경로
    path('first/', views.boardfirst)
]