from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.db.models import Q

from movies.models import Movie, Rating
from users.forms import GiveRatingForm


class MovieDetailView(DetailView):
    model = Movie

    def post(self, request, *args, **kwargs):
        form = GiveRatingForm(request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.movie = Movie.objects.get(pk=self.kwargs['pk'])
            form.save()
        return redirect(request.path)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if i := Rating.objects.filter(movie=self.kwargs['pk']).filter(user=self.request.user).first():
                context['user_rating'] = getattr(i, 'rating')
        context["now"] = timezone.now()
        context["form"] = GiveRatingForm()
        return context


class MovieListView(ListView):
    model = Movie
    paginate_by = 12  # if pagination is desired

    def get_queryset(self):
        query = self.request.GET.get('name')
        if query:
            return self.model.objects.filter(Q(primaryTitle__icontains=query) | Q(genres__icontains=query))
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('name'):
            context['name'] = self.request.GET.get('name')
        context["now"] = timezone.now()
        return context