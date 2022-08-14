from django.urls import path, include
from posts.views import PostList, PostDetail

postspatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()), 
]
urlpatterns = [
    path('posts/', include(postspatterns)),
    
]

