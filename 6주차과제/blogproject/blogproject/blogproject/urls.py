from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'), # name space를 정해주는 것이 중요 
    
    # html form을 이용해 블로그 객체 만들기 
    path('new/',views.new, name='new'),
    path('creat/',views.creat, name='creat'),

    # django form을 이용해 블로그 객체 만들기 
    path('formcreat/',views.formcreat, name='formcreat'),

    # django modelform을 이용해 블로그 객체 만들기 
    path('modelformcreat/',views.modelformcreat, name='modelformcreat'),

    # http://127.0.0.1:8000/detail/1(=pk값)
    # http://127.0.0.1:8000/detail/2 
    path('detail/<int:blog_id>',views.detail, name='detail'), # <int:blog_id>는 pk값인 post.id를 blog_id에 담아 views.py에 detail함수에 넘겨줌

    path('creat_comment/<int:blog_id>',views.creat_comment, name='creat_comment'),

    path('login/',accounts_views.login, name='login'),
    path('logout/',accounts_views.logout, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
