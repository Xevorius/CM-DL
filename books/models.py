from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg, Count


class Genre(models.Model):
    label = models.CharField(max_length=100)


class Book(models.Model):
    ISBN = models.CharField(max_length=100)
    bookTitle = models.CharField(max_length=100)
    yearOfPublication = models.IntegerField(blank=True, null=True)
    imageUrl = models.CharField(max_length=200, blank=True, null=True)
    genres = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)

    def average_rating(self):
        rating = BookRating.objects.filter(book=self).aggregate(avarage=Avg('rating'))
        if rating["avarage"] is not None:
            return float(rating["avarage"])
        return 0

    def count_ratings(self):
        reviews = BookRating.objects.filter(book=self).aggregate(count=Count('id'))
        if reviews["count"] is not None:
            return int(reviews["count"])
        return 0

    def __str__(self):
        return f"{self.id} - {self.bookTitle}"


class BookRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])

    def __str__(self):
        return f"{self.user} - {self.book}"


class BookAuthor(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} - {self.author}"

