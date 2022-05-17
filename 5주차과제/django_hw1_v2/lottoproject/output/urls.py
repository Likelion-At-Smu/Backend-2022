from django.urls import path
from output import views

urlpatterns = [
    path('', views.output, name='compute'),
]
