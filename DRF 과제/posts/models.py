from django.conf import settings
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)




class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%d: %s' % (self.order, self.title)

# Create your models here.
