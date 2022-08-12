from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model) :
    title = models.CharField(verbose_name='내용', max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)