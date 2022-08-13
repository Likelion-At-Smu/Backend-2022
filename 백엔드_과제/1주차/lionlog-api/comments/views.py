from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from comments.models import Comment
from comments.serializers import CommentSerializer

class CommentList(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        comment = self.get_object(pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
