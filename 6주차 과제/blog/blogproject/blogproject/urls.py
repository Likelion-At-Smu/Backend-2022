"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 

    #html form을 이용할 path
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    #django form을 이용할 path
    path('djangonew/', views.djangonew, name='djangonew'),

    #model form을 이용할 path
    path('modelnew/', views.modelnew, name='modelnew'),

    #/detail/id_value
    path('detail/<int:id>', views.detail, name='detail'),

    #댓글 작성 path
    path('createcomment/<int:post_id>', views.createcomment, name='createcomment'),

    #로그인 path
    path('login/', accounts_views.login, name='login'),

    #로그아웃 path
    path('logout/', accounts_views.logout, name='logout')
] 

#미디어 경로를 url패턴에 추가
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
