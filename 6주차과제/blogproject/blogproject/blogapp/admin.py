from django.contrib import admin
from .models import Blog, Comment

# admin 사이트에서 객체 확인 가능
admin.site.register(Blog)
admin.site.register(Comment)