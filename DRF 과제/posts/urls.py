from django.urls import path, include
from . import views
urlpatterns = [
    # path('posts/', views.post_list),
    # path('posts/<int:pk>', views.post_detail)

    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),

    path('posts/comments/', views.CommentList.as_view()),
    path('posts/comments/<int:pk>/', views.PostComment.as_view())
]
