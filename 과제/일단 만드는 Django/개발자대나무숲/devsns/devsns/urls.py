from django.contrib import admin
from django.urls import path, include
from snsapp import views
from accounts import views as accounts_views
# url이 많을경우, app별로 urls.py를 만들어 include로 url을 계층적으로 관리하는 것이 더 효율적 
# 이번에는 그냥 해쓰요

urlpatterns = [
    path('admin/', admin.site.urls),

    # 익명게시판 
    path('', views.home, name='home'),
    path('postcreat/',views.postcreat, name='postcreat'),
    # post_id를 detail 함수에 인자로 전달
    path('detail/<int:post_id>',views.detail, name='detail'),
    path('new_comment/<int:post_id>',views.new_comment, name='new_comment'),

    path('login/',accounts_views.login, name='login'),
    path('logout/',accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),

    # 자유게시판
    path('freehome/', views.freehome, name='freehome'),
    path('freepostcreate', views.freepostcreate, name='freepostcreate'),
    path('freedetail/<int:post_id>', views.freedetail, name='freedetail'),
    path('new_freecomment/<int:post_id>', views.new_freecomment, name='new_freecomment'),

    path('accounts/', include('allauth.urls')),

]
