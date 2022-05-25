# $python manage.py migrate를 통해 먼저 직접 데이터베이스에 반영되지 않은 객체를 반영
# python manage.py makemigrations를 통해 실제 데이터 베이스에 반영
from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models

# Model 상속
# python manage.py makemigirations 를 통해 변경사항 담긴 파일 만들어줌
class Blog(models.Model):
    title = models.CharField(max_length=200)  # 최대길이지정
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo') # media/blog_photo에 자동으로 저장
    date = models.DateTimeField(auto_now_add=True) # auto_now_add=True 자동으로 현재 시간 추가

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True) # 자동으로 현재 시간 추가
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
