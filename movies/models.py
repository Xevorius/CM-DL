from django.db import models


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

