from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('second/', views.second),

    # products로 시작하는 url은 include 내의 경로의 urls.py가 담당할 것.
    path('products/', include('product.urls')),

    # boards도 마찬가지.
    # include를 import해서 app별로 url 설정이 가능.
    path('boards/', include('board.urls'))
]
