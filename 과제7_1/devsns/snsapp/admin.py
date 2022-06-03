from django.contrib import admin
from .models import Post, Comment, FreePost,FreeComment
# models.py로 부터 Post를 가져올건데
# 그것을 admin.site에 등록할 것 이다
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FreePost)
admin.site.register(FreeComment)