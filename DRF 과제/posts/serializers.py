from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    # post = serializers.ModelField(model_field=Post._meta.get_field('id'), read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        # pathvariable로 댓글을 작성할 때 필요한 옵션
        # read_only_fields = ['post']


class PostSerializer(serializers.ModelSerializer):

    #변수 명은 역참조하는 모델의 필드에 related_name 옵션의 value로 설정해야 한다.
    #comment의 모든 field를 불러오기 위해 Nested relationships를 사용했다.
    #Relatedfield를 사용하는 방법도 있지만
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'writer', 'comments']

