from django.urls import path, include
from posts.views import PostList, PostDetail

urlpatterns = [
    # path('posts/', post_list),
    # path('posts/<int:pk>', post_detail),

    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
]