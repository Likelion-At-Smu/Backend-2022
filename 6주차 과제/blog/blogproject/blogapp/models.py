from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models

class Blog(models.Model):
    #속성들의 타입과 제약사항을 설정
    #primary key를 지정해주지 않았기 때문에 id라는 기본키를 django가 추가함
    title = models.CharField(max_length=200)
    body = models.TextField()
    #pip로 pillow를 설치해줘야했음
    photo = models.ImageField(blank=True, null=True, upload_to = 'blog_photo')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
       return self.comment

#데이터 클래스를 만든 후 makemigrations 명령어를 통해 해당 파일을 만들고 migrate로 DB에 정보를 반영해야함.
# Create your models here.
