from .models import Book, Url
from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    class Meta:
        model = Book
        fields = "__all__"

class UrlSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(read_only=True)
    class Meta:
        model = Url
        fields = ("long_url", "short_url",)
