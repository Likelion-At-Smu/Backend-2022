# python manage.py createsuperuser를 통해 admin계정 생성

from django.contrib import admin
from .models import Blog, Comment

# http://127.0.0.1:8000/admin 에서 Blog객체 확인가능 
admin.site.register(Blog)
admin.site.register(Comment)