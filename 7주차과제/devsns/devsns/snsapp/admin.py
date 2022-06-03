from django.contrib import admin
from .models import Post, Comment, FreePost, FreeComment

# admin 사이트에서 객체 확인 가능
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FreePost)
admin.site.register(FreeComment)