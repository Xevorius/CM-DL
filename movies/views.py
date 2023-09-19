from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from movies.models import Movie


class MovieDetailView(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class MovieListView(ListView):
    model = Movie
    paginate_by = 12  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context