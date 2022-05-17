from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', views.lotto, name='start'),
    path('lotto/result/', views.result, name='compute'),
]
