from django.shortcuts import render
from .models import Book
from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class AccountBooklist(APIView):
    permissions_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # 가계부 리스트
    def get(self, request):
        user = User.objects.get(pk=request.user.pk)
        my_books = []
        books = Book.objects.filter(user_id=user)
        for book in books:
            my_books.append(book)
        serializer = BookSerializer(my_books, many=True)
        return Response(serializer.data)

    # 새로운 가계부를 작성
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.validated_data["user"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountBookDetail(APIView):
    permissions_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # 가계부 세부 내역
    def get(self, request, pk, format=None):
        book = Book.objects.get(pk=pk)
        if book.user == request.user:
            serializer = BookSerializer(book)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 가계부 세부 내역 복제
    def post(self, request, pk, format=None):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(data={'id': book.id, 'user': book.user, 'price': book.price, 'memo': book.memo, 'note_at': book.note_at})
        if serializer.is_valid():  # 유효성 검사
            serializer.validated_data["user"] = request.user
            serializer.save()
            return Response('copy success!')
    # 가계부 수정
    def put(self, request, pk, format=None):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if book.user == request.user:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 가계부 삭제
    def delete(self, request, pk, format=None):
        book = Book.objects.get(pk=pk)
        if book.user == request.user:
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
