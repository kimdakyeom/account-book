from django.shortcuts import render
from .models import Book
from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class AccountBooklist(APIView):
    # permissions_classes = [IsAuthenticated]
    # 가계부를 보여줄 때
    def get(self, request):
        user = User.objects.get(pk=request.user.pk)
        my_books = []
        books = Book.objects.filter(user_id=user)
        for book in books:
            my_books.append(book)
        serializer = BookSerializer(my_books, many=True)
        return Response(serializer.data)

    # 새로운 가계부를 작성할 때
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.validated_data["user"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountBookDetail(APIView):
    def get(self, request, pk, format=None):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)