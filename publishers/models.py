from django.db import models

from books.models import Book


class Publisher(models.Model):
    publisherName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.publisherName}"


class BookPublisher(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} - {self.publisher}"