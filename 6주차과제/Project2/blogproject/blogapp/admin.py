from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Blog, Comment

# 우리가 정의해준 models.py 담긴 내용을 볼 수 있음
admin.site.register(Blog)
#admin 계정을 만들어줘야 함
# python manage.py createsuperuser

admin.site.register(Comment)