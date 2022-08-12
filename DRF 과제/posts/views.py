from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# @api_view(['GET', 'POST'])
# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', "DELETE"])
# def post_detail(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "PUT":
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.update(instance=post, validated_data=serializer.validated_data).save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "DELETE":
#         post.delete()
#         return Response(status=status.HTTP_200_OK)

class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return post

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            print(serializer.save())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_200_OK)


class CommentList(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostComment(APIView):
    def get_object(self, pk):
        return get_object_or_404(Comment, pk=pk)
    #게시글 안에서 댓글 작성, 수정, 삭제가 일어나서 해당 클래스에 작성, 수정, 삭제를 포함하는게 좋다고 생각했음
    #구현하고 보니 pk에 대한 일관성이 떨어져서 오히려 혼동이 생길듯 함.
    #프론트로부터 post pk를 json data로 요청받는게 더 좋다는 결론
    # def post(self, request, post_pk, format=None):
    #     post = Post.objects.get(pk=post_pk)
    #
    #     serializer = CommentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(post=post)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format = None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_200_OK)





# Create your views here.
