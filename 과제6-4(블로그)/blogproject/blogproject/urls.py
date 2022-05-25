from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    #html form을 이용해서 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    #django form을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),
#django는 사람으로 부터 입력값을 받을 수 있는 url이 있으면
# 이 한 url에 대해서 GET요청과 POST 요청을 둘 다 할 수 있다

    #django modelform을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    path('detail/<int:blog_id>', views.detail, name='detail'),
    # 같이 넘어온  블로그 id값은 정수형태이고 그 정보를  blog_id라는 변수 이름에 담아서 detail 함수에 넘길 값
    #detail만 이아니라 몇번째 블로글에 해당하는지 id값이 필요하므로
    # 추가적인 정보가 필요 ==> primary key값을 추가적으로 넘겨줘야 알아들어 
    # html을 띄워준다

# http://127.0.0.1:8000/detail/1
# http://127.0.0.1:8000/detail/2
# http://127.0.0.1:8000/detail/3

    path('create_comment/<int:blog_id>', views.create_comment, name='detail'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),


]
 # media 파일에 접근할 수 있는 url도 추가해줘야함

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
