from django.urls import path
from product import views

urlpatterns = [
    path('',views.productlist), # 127.0.0.1/8000/products/
    path('first/',views.productfirst) # 127.0.0.1/8000/products/first 일 때
]

# 1/, 2/, 3/ 이렇게 자동화 시키는 방법도 존재 ! 