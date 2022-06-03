from django.contrib import admin
from django.urls import path, include
from snsapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('postcreate', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    #detail/ int형으로 받을건데 post_id라는 변수로써 detail이라는 함수에 인자로 넘겨준다
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),

    path('login/', accounts_views.login, name='login'),    
    path('logout/', accounts_views.logout, name='logout'),

    path('freehome/', views.home, name='home'),
    path('freepostcreate', views.freepostcreate, name='freepostcreate'),
    path('freedetail/<int:post_id>', views.freedetail, name='freedetail'),
    path('new_freecomment/<int:post_id>', views.new_freecomment, name='new_freecomment'),
    path('signup/', accounts_views.signup, name='signup'),

    path('', views.freehome, name='freehome'),
    path('accounts/', include('allauth.urls')),


]