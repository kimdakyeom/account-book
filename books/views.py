from django.shortcuts import render
from .models import Book
from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
import pyshorteners as ps

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
            return Response('copy success!', status=status.HTTP_201_CREATED)
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

# 단축 url 생성
class ShortUrl(APIView):
    def post(self, request, pk, format=None):
        serializer = UrlSerializer(data=request.data)
        urls = Url.objects.all()
        url = []
        for u in urls:
            url.append(u.long_url)
        if serializer.is_valid():
            link = serializer.validated_data["long_url"]
            # db에 저장 안되있으면 새로 생성해서 저장
            if link not in url:
                sh = ps.Shortener()
                short_url = (sh.tinyurl.short(link))
                serializer.validated_data["short_url"] = short_url
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # db에 저장 되어있으면 해당 데이터 보여주기
            else:
                url_data = Url.objects.get(long_url=link)
                return Response({"long_url":link, "short_url":url_data.short_url})