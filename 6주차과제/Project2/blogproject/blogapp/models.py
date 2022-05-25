from tkinter import CASCADE
from django.db import models

# Model 상속
# python manage.py makemigirations 를 통해 변경사항 담긴 파일 만들어줌
class Blog(models.Model):
    title = models.CharField(max_length=200)  # 최대길이지정
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo') # 비어있는 값으로 줘도 괜찮, media/blog_photo에 자동으로 저장
    date = models.DateTimeField(auto_now_add=True) # 자동으로 지금 시간 추가


    # title이 나타나도록
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True) # 자동으로 지금 시간 추가
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
