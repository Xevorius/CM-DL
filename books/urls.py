from django.urls import path

from books.views import BookDetailView, BookListView

urlpatterns = [
    path("book/<pk>/", BookDetailView.as_view(), name="book-detail"),
    path("", BookListView.as_view(), name="book-list"),
]