from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as account_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # django form을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    # django model form을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    # 뒤에 추가적인 정보 int형태 blog_id에 담아서 
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('create_comment/<int:blog_id>', views.create_comment, name='create_comment'),
    path('login/', account_views.login, name='login'),
    path('logout/', account_views.login, name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 이런식으로도 씀 
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)