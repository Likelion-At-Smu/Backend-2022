# from tkinter import CASCADE
from django.db import models

class Blog(models.Model):  #블로그 model
    title = models.CharField(max_length=200) 
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)
    # (자동으로 지금 시간을 추가하겠다)의 의미
    # 변경사항이 있으면 변경사항이 담긴 파일을 담아줘야한다


#primary key 값을 지정해주지 않으면 id라는 숫자로 이루어진 숨겨진key 값을 만들어놓는다

    def __str__(self): #admin  사이트에서 글의 제목이 뜨도록 한다
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    #게시물에 달린 댓글도 함께 삭제 되야 하므로 
    # 블로그가 삭제 된다면 on_delte 거기에 달려있는 그 게시물에 참조 하고 있는 comment 객체도
    # 함께 삭제된다는 의미
    # 어떤 게시물에 달려 있는 댓글인지를 알 수 있는 , 댓글이 달린 게시물에 쓰임
    #다른 table을 참조할 수 있는 키 는 외래 키
    def __str__(self): #admin  사이트에서 글의 제목이 뜨도록 한다
        return self.comment 
        #comment를 반환하도록 시킨다d
