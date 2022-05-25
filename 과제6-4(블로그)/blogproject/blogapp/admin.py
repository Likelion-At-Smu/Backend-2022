from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Blog)
admin.site.register(Comment)
#데이터 베이스 안에 있는 데이터를 보려면
# admin 사이트에 등록해라 comment를