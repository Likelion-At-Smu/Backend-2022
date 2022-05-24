from django.urls import path
from product import views

urlpatterns = [
    # 127.0.0.1:8000/products/의 경로
    path('', views.productlist),

    # 127.0.0.1:8000/products/first/의 경로
    path('first/', views.productfirst)
]