from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as accounts_view
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

     # django modelform을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    # 몇 번째에 해당하는 블로그 글인지 같이 인자를 넘겨줘야 함
    path('detail/<int:blog_id>', views.detail, name='detail'),

    # 댓글 저장하는 url
    path('create_comment/<int:blog_id>', views.create_comment, name='create_comment'),

    path('login/', accounts_view.login, name='login'),
    path('logout/', accounts_view.logout, name='logout')

    # media 파일 접근할 수 있는 url 추가하는 방법. urlpatterns 자체에다 추가해야 함
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
