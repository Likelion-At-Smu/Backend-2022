from tkinter import CASCADE
from django.db import models

#블로그 객체 생성
class Blog(models.Model):
    # 제목 최대 길이도 제한해줄 수 있음
    title = models.CharField(max_length=200)
    body = models.TextField()
    # upload_to : 파일 저장되는 경로 지정 -> media/blog_photo
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    # auto_now_add = True 자동으로 지금 시간 추가
    date = models.DateTimeField(auto_now_add=True)
    # pk 지정 안하면 django가 자동으로 id라는 pk를 생성
    # id = 1

    # 목록에서 객체가 title로 보이게 함
    def __str__(self):
        return self.title

class Comment(models.Model):
    # comment = models.CharField()
    # 더 크게(길게) 적어주게 하고 싶으면 아래와 같이 적음
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 댓글이 어떤 게시글의 달려있는 댓글인지 알아야 하므로 Blog 객체 참조
    # 게시글 삭제되면 댓글도 같이 삭제되어야 하므로 on_delete=models.CASCADE
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment