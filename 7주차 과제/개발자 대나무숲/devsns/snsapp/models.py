from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#모델 파일 생성 후 makemigrations
#migration 파일 생성 후 migrate
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#1.models.py에 모델을 만든다.
#2.forms.py에 form을 만든다.
#3.views로 해당 폼을 입력할 수 있는 폼을 html로 보내준다.
#4.사용자가 폼에 입력하면 입력한 정보를 저장한다.
class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
# Create your models here.


class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#자유게시판 댓글에도 작성자를 추가함
class FreeComment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)