"""cafeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cafeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('detail1/', views.detail, name='detail1'),
    path('detail2/', views.detail, name='detail2'),
    path('detail3/', views.detail, name='detail3'),
    path('detail4/', views.detail, name='detail4'),
    path('detail5/', views.detail, name='detail5'),
    path('detail6/', views.detail, name='detail6'),
    path('detail7/', views.detail, name='detail7'),
    path('detail8/', views.detail, name='detail8'),
    path('detail9/', views.detail, name='detail9'),


]
