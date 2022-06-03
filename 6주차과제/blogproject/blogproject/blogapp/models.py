from django.db import models
from tkinter import CASCADE
from distutils.command.upload import upload

# class로 정의, models안에 Model을 상속(=이미 구현되어 있는 장고의 모델 기능을 사용)
# Blog 모델 
class Blog(models.Model) : 
    # 어떤형식을 지정해 줄 것인지 models.으로 나타내줘야함 !
    title = models.CharField(max_length=200)  
    body = models.TextField()
    photo = models.ImageField(blank=True,null=True,upload_to='blog_photo') # media/blog_photo에 자동으로 저장
    date = models.DateTimeField(auto_now_add=True) # 자동으로 지금시간 추가

    def __str__(self) :
        return self.title # admin사이트에서 blog object(1)이런식으로 써있는 걸 title명으로 바꿈


class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True) # 자동으로 현재 시간 추가
    post = models.ForeignKey(Blog, on_delete=models.CASCADE) # 어떤 게시물에 있는 댓글인 지, FK(외래키)로 만들어줘야함 
                                                             # Blog라는 객체 참조, on_delete(=삭제된다면) 같이 삭제 
    
    def __str__(self):
        return self.comment

# db에 변경사항이 생김(Blog모델 추가) 
# 데이터베이스 변경사항이 담긴 파일을 만들어줌 python manage.py makemigrations
# python manage.py migrate 데이터베이스에 반영 

