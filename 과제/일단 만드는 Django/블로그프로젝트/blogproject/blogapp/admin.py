from django.contrib import admin
from .models import Blog, Comment

# Register your models here.

# admin site에서 블로그, 코멘트 객체 확인 가능
admin.site.register(Blog)
admin.site.register(Comment)