from django.contrib import admin
from django.urls import path
from movieapp import views

urlpatterns = [
    path('adminsuuuujin/', admin.site.urls),
    path('', views.home, name='home'),
    # o.id가 정수가 아닌 문자열임
    path('detail/<str:movie_id>/', views.detail, name='detail'),
]