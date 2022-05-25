from django.db import models

# Create your models here.

#table의 작성
class Blog(models.Model):
    #최대길이 설정
    title = models.CharField(max_length=200)
    body = models.TextField()
    #media file 을 media/blog_photo에 upload
    photo = models.ImageField(blank = True, null=True, upload_to = 'blog_photo')
    #자동 시간 설정
    date = models.DateTimeField(auto_now_add=True)
    
    #제목을 표시하기 위한 함수
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    
    data = models.DateTimeField(auto_now_add=True)
    # 어떤 게시물에 달려있는 댓글인지를 알 수 있는, 댓글이 달린 그 게시물이 쓰임
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment