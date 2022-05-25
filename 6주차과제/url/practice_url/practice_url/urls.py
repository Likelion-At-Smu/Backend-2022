from itertools import product
from django.contrib import admin
from django.urls import path, include # include는 계층적으로 이루어진 url을 
from myapp import views # 이거 써주는거 까먹지 말기 !! myapp에서부터 views에 있는 내용을 가져와야 실행됨 !

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first), # 8000/ 뒤에 아무것도 없을 때 -> viesw에 있는 first라는 함수를 실행
    path('second/', views.second),
    path('products/',include('product.urls')), # products/ 로 시작해 products/1, products/2 이런 아이들은 product.urls을 통해 관리 !
    path('boards/',include('board.urls')), # boards/ 로 시작하는 건 '우리가 직접 만들어 준' board파일 안에 urls.py에서 관리 ! 
]


# 아래와 같이 계층적으로 이루어진 url
    # 127.0.0.1:8000/products/1
    # 127.0.0.1:8000/products/2
    # 127.0.0.1:8000/products/3
    # ...
# 이를 간단히하기 위해 app과 include를 이용 ! -> app을 만들고 그 폴더 안에 urls.py를 만들고, urlpatterns에 등록 !
