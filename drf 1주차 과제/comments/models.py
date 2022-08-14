from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to='posts.Post', related_name = "comments",on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)