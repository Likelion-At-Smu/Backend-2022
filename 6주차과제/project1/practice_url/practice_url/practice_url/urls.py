from django.contrib import admin
from django.urls import path, include
from myapp import views

# 계층적으로 이루어진 url을 application을 통해서 효율적으로 관리
# include, app안에 urls.py
# products/라는 path 하에서는 모두 product.urls에서 관리
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('second/', views.second),
    path('products/', include('product.urls')),
    path('boards/', include('board.urls')),
]
