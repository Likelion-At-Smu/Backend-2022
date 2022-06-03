# db에 변경사항이 생기면(모델 추가) 
# 데이터베이스 변경사항이 담긴 파일을 만들어줌 python manage.py makemigrations
# python manage.py migrate 데이터베이스에 반영 

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# class로 정의, models안에 Model을 상속(=이미 구현되어 있는 장고의 모델 기능을 사용)
# 게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=200) 
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True) # 자동으로 현재 시간 추가
    post = models.ForeignKey(Post,null=True, blank=True, on_delete=models.CASCADE) # 어떤 게시물에 있는 댓글인 지, FK(외래키)로 만들어줘야함 
                                                        # POST 객체 참조, on_delete(=삭제된다면) 같이 삭제 

    def __str__(self):
        return self.comment

# 자유게시판 
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 유저인지에 대한 정보 
    author =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE) # 자유게시판을 참조 

    def __str__(self):
        return self.comment