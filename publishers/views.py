from django.db.models import Q
from django.utils import timezone
from django.views.generic import DetailView, ListView

from publishers.models import Publisher, BookPublisher


class PublisherDetailView(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('name'):
            context['name'] = self.request.GET.get('name')
        context["now"] = timezone.now()
        context["books"] = BookPublisher.objects.filter(publisher_id=self.kwargs['pk'])
        # context["authors"] =
        return context


class PublisherListView(ListView):
    model = Publisher
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('name')
        if query:
            return self.model.objects.filter(Q(publisherName__icontains=query))
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('name'):
            context['name'] = self.request.GET.get('name')
        context["now"] = timezone.now()
        return context
