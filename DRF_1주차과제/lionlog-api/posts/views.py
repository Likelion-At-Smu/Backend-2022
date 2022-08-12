from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostSerializer

from posts.models import Comment
from posts.serializers import CommentSerializer

# @api_view(['GET','POST'])
# def post_list(request) :
#     if request.method == 'GET' :
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     elif request.method =='POST' :
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid() :
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def post_detail(request, pk) :
#     try :
#         post = Post.objects.get(pk=pk)
#     except :
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET' :
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == 'PUT' :
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid() :
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE' :
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# POST
class PostList(APIView) :
    def get(self, request, format=None) :
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None) :
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView) :
    def get_object(self, pk) :
        try :
            return Post.objects.get(pk=pk)
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk, format=None) :
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None) :
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None) :
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# COMMENT
class CommentList(APIView) :
    def get(self, request, format=None) :
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    def post(self, request, format=None) :
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView) :
    def get_object(self, pk) :
        try :
            return Comment.objects.get(pk=pk)
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk, format=None) :
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None) :
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None) :
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


