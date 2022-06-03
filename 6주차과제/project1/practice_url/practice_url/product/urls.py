from django.urls import path
from product import views

# products/ 하에서 실행되는 url들
urlpatterns = [
    path('', views.productlist), # products/
    path('first/', views.productfirst) # products/first/
]
