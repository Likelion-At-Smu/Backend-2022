from django.urls import path
from board import views

# boards/ 하에서 실행되는 url들
urlpatterns = [
    path('', views.board), # = boards/ 
    path('first/', views.boardfirst), # = boards/first/
]
