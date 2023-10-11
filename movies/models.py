from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg, Count


class Movie(models.Model):
    tconst = models.CharField(max_length=100)
    titleType = models.CharField(max_length=100)
    primaryTitle = models.CharField(max_length=100)
    originalTitle = models.CharField(max_length=100)
    isAdult = models.BooleanField()
    startYear = models.IntegerField(blank=True, null=True)
    endYear = models.IntegerField(blank=True, null=True)
    runtimeMinutes = models.IntegerField(blank=True, null=True)
    genres = models.CharField(max_length=100)

    def average_rating(self):
        rating = MovieRating.objects.filter(movie=self).aggregate(avarage=Avg('rating'))
        if rating["avarage"] is not None:
            return float(rating["avarage"])
        return 0

    def count_ratings(self):
        reviews = MovieRating.objects.filter(movie=self).aggregate(count=Count('id'))
        if reviews["count"] is not None:
            return int(reviews["count"])
        return 0


class MovieRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
