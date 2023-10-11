from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.db.models import Q

from books.models import Book, BookRating, BookAuthor
from publishers.models import BookPublisher, Publisher
from users.forms import GiveBookRatingForm


class BookDetailView(DetailView):
    model = Book

    def post(self, request, *args, **kwargs):
        form = GiveBookRatingForm(request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.book = Book.objects.get(pk=self.kwargs['pk'])
            form.save()
        return redirect(request.path)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if i := BookRating.objects.filter(book=self.kwargs['pk']).filter(user=self.request.user).first():
                context['user_rating'] = getattr(i, 'rating')
        context['author'] = User.objects.get(pk=getattr(BookAuthor.objects.filter(book=self.kwargs['pk']).first(), 'author_id'))
        context['publisher'] = Publisher.objects.get(pk=getattr(BookPublisher.objects.filter(book=self.kwargs['pk']).first(), 'publisher_id'))
        context["now"] = timezone.now()
        context["form"] = GiveBookRatingForm()
        return context


class BookListView(ListView):
    model = Book
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('name')
        if query:
            return self.model.objects.filter(Q(bookTitle__icontains=query))
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('name'):
            context['name'] = self.request.GET.get('name')
        context["now"] = timezone.now()
        return context
