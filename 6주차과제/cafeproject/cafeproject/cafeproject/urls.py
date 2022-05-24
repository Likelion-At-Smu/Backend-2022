from django.contrib import admin
from django.urls import path
from cafeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url 바로 접속했을 때 home 함수 실행
    path('', views.home, name='home'),
    # detail/로 갔을 때는 detail 함수 실행
    path('detail/', views.detail, name='detail'),
]
