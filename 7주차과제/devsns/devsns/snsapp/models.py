from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# 게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # auto_now_add=True 그 당시 시간 반영
    date = models.DateTimeField(auto_now_add=True)

    # 목록에 제목이 보이게
    def __str__(self):
        return self.title

# 클래스를 이용해서 데이터베이스를 매핑하는 모델
#ORM: Object Oriented Mapping
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시글의 댓글인지 알기 위해 Post 참조
    # on_delete=models.CASCADE : post 삭제되면 comment도 삭제
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # auto_now_add=True 그 당시 시간 반영
    date = models.DateTimeField(auto_now_add=True)
    # User 객체 참조
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 목록에 제목이 보이게
    def __str__(self):
        return self.title

class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시글의 댓글인지 알기 위해 Post 참조
    # on_delete=models.CASCADE : post 삭제되면 comment도 삭제
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
