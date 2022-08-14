from django.urls import path, include
from .views import *

commentspatterns = [
    path('', CommentList.as_view()),
    path('<int:pk>/', CommentDetail.as_view()), 
]
urlpatterns = [
    path('posts/comments/', include(commentspatterns)),
    
]


