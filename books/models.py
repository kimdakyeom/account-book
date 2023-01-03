from django.db import models
from django.conf import settings

class Book(models.Model):
    price = models.IntegerField()
    memo = models.CharField(max_length=150)
    note_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="book_user"
    )

class Url(models.Model):
    long_url = models.CharField(max_length=300)
    short_url = models.CharField(max_length=200)