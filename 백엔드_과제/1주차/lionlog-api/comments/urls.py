from django.urls import path
from comments.views import CommentList, CommentDetail

urlpatterns = [
    path('', CommentList.as_view()),
    path('<int:pk>', CommentDetail.as_view()),    
]