from django.contrib import admin
from .models import Post, Comment, FreePost, FreeComment

#게시물 모델 등록
admin.site.register(Post)
# 댓글 모델 등록
admin.site.register(Comment)
admin.site.register(FreePost)
admin.site.register(FreeComment)
