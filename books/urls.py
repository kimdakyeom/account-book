from django.urls import path, include
from . import views
app_name = 'books'

urlpatterns = [
    path("", views.AccountBooklist.as_view()),
    path("<int:pk>", views.AccountBookDetail.as_view())
]