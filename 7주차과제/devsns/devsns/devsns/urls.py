from django.contrib import admin
from django.urls import path, include
from snsapp import views
from accounts import views as accounts_views

# url 많을 경우 app 별로 urls.py 만들어 include로 계층적 관리하는 것이 더 좋음
# 이 프로젝트는 url 갯수 적으니 하나의 urls.py에서 관리

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('postcreate/', views.postcreate, name='postcreate'),

    # post.id 인자를 post_id라고 하는 변수명으로서 detail함수에다가 인자로 넘겨줌
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('new_comment/<int:post_id>/', views.new_comment, name='new_comment'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),

    # home, postcreate, detail, new_comment와 동일
    path('freehome', views.freehome, name='freehome'),
    path('freepostcreate/', views.freepostcreate, name='freepostcreate'),
    path('freedetail/<int:post_id>/', views.freedetail, name='freedetail'),
    path('new_freecomment/<int:post_id>/', views.new_freecomment, name='new_freecomment'),

    #소셜 로그인 기능 구현
    path('accounts/', include('allauth.urls')),
]
