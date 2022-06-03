from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User

# 게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # 화면에 title을 띄워라
    def __str__(self):
        return self.title

# 댓글 객체
class Comment(models.Model):
    # 내용 자체에대한 부분
    comment = models.TextField()
    # 댓글 작성 날짜
    date = models.DateTimeField(auto_now_add=True)
    # 어느 게시물에 달린 댓글인지 알기 위해서 foreign key를 선언
    # post늘 Post를 참조하고 있고 삭제 제약조건이 있다.
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    # admin page에서 확인할 수 있게 하기 
    def __str__(self):
        return self.comment

# 자유게시판
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 익명이 아니기 때문에 작성자 추가, django에 내장된 user객체를 참조해서 만들기
    author =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# 자유게시판에서 사용하는 댓글
class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment