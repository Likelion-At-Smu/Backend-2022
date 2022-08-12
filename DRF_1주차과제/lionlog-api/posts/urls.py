from django.urls import path, include
from posts.views import PostList, PostDetail 
# from posts.views import post_list, post_detail
from posts.views import CommentList, CommentDetail

urlpatterns = [
    # path('posts/', post_list),
    # path('posts/<int:pk>', post_detail),

    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('posts/comments/',CommentList.as_view()),
    path('posts/comments/<int:pk>',CommentDetail.as_view())
]

# Django : settings.py -> Model -> urls.py -> views.py -> templates
# DRF : settings.py -> Model -> serializer(model을 json형태로 반환) -> urls.py -> views.py