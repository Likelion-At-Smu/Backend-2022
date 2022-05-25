from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Blog)

admin.site.register(Comment)