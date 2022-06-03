from django.contrib import admin
from .models import FreeComment, FreePost, Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FreePost)
admin.site.register(FreeComment)
