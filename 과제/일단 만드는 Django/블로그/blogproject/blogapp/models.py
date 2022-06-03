from django.db import models

# Create your models here.

class Blog(models.Model): # models 안에 Model을 상속
    title = models.CharField(max_length=100)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now=True) # 자동으로 현재 시간을 추가
    # id 값을 따로 지정하지 않으면 django는 PK를 자동으로 지정함

    # admin site에서 글 이름으로 목록 확인 가능
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시물의 댓글인지 알 수 있도록 함
    # Blog 객체를 참조하는 FK
    # CASCADE -> 참조하는 대상이 삭제되면 삭제된다는 뜻
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    # admin site에서 comment 내용을 제목으로 한 목록이 뜨도록 함
    def __str__(self):
        return self.comment