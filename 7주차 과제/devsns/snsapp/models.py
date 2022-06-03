from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):#타이틀 출력하기 위한 함수
        return self.title

class Comment(models.Model):#오브젝트 오리엔티드 맵핑 ORM 코멘트 모델
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)#포스트라는 컬럼에 종속적으로 만든다.
    #CASCADE => POST가 삭제되면 같이 삭제됨.
    def __str__(self):
        return self.comment

class FreePost(models.Model):#자유게시판 게시물
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)#자유게시판이므로 작성자에 해당하는 정보가 있어야된다.
    #데이터베이스에서 유저가 탈퇴한다면 이 작성자가 작성한 게시물과 댓글이 사라진다.

    def __str__(self):
        return self.title

class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment