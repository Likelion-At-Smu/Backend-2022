from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#테이블로 삼고자하는 모델을 정의해야한다
#게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #auto_now_add=True로 인해 객체가 추가될때마다 그 당시의 시간이 추가된다

    def __str__(self):
        return self.title # 글을 등록했을 때 글작성시 사용한 제목이 보이도록

class Comment(models.Model): # 클래스 이용해서 데이터베이스에 맵핑하는 것은 orm 
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    #post가 참조하는 데이터가 삭제되면 (on_delte ) 참조하고 있는 이 객체도 같이 삭제될 것이다
    
    def __str__(self):
        return self.comment # 글을 등록했을 때 글작성시 사용한 제목이 보이도록

class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #auto_now_add=True로 인해 객체가 추가될때마다 그 당시의 시간이 추가된다

    def __str__(self):
        return self.title # 글을 등록했을 때 글작성시 사용한 제목이 보이도록


class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 유저의 객체를 author에 담아주어야 한다 author은 유저 객체들로 이루어진 컬럼이므로
    author = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)
    #auto_now_add=True로 인해 객체가 추가될때마다 그 당시의 시간이 추가된다

    def __str__(self):
        return self.comment # 글을 등록했을 때 글작성시 사용한 제목이 보이도록


