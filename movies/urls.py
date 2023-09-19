from django.urls import path

from movies.views import MovieDetailView, MovieListView

urlpatterns = [
    path("movie/<pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("", MovieListView.as_view(), name="movie-list"),
]