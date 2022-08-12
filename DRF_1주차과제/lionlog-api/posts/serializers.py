from dataclasses import field
from rest_framework import serializers
from posts.models import Post
from posts.models import Comment

class CommentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Comment
        #fields = ['content','created_at','writer']
        fields = ['content','created_at','post','writer']


class PostSerializer(serializers.ModelSerializer) :   
    comments = CommentSerializer(many=True, read_only=True)
    class Meta :
        model = Post
        #fields = "__all__"
        fields = ['id','title','content','create_at','comments','writer']