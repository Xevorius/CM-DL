from django.db import models

from books.models import Book


class Publisher(models.Model):
    publisherName = models.CharField(max_length=100)


class BookPublisher(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)