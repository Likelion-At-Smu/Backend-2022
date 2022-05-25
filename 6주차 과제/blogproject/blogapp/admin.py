from django.contrib import admin
from .models import Blog, Comment
# Register your models here.

#admin site에서 object의 내용을 확인한다.
admin.site.register(Blog)
admin.site.register(Comment)